from flask import Flask, render_template, request, Response
import gevent
import gevent.monkey
from gevent.pywsgi import WSGIServer
from gevent import sleep
gevent.monkey.patch_all()
import time
from kinet import *
import re

app = Flask(__name__)

#global currentNum
currentNum = 0
currentColor = '#FFFFFF'

print "Adding fixtures..."
pds = PowerSupply('10.0.0.154')
fix1 = FixtureRGB(0)
pds.append(fix1)
fix2 = FixtureRGB(3)
pds.append(fix2)
fix3 = FixtureRGB(6)
pds.append(fix3)
fix4 = FixtureRGB(9)
pds.append(fix4)
fix5 = FixtureRGB(12)
pds.append(fix5)

fixtures ={'0':'0', '3':'0', '6':'0', '9':'0', '12':'0'}

print "Fixtures ready!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def nofavicon():
    return '', 204




def event_stream():
    global currentNum
    print currentNum
    setNum = 0
    while True:
        if setNum != currentNum:
            yield 'data: %s\n\n' % currentNum
            setNum = currentNum
        gevent.sleep(0.1)



def streamColor(fix):
    global fixtures
    lastColor = ''
    while True:
        if lastColor != fixtures[fix]:
            yield 'data: %s\n\n' % fixtures[fix]
            lastColor = fixtures[fix]
        gevent.sleep(0.1)


@app.route('/setColor/<fix>/<color>')
def setColor(fix, color):
    global currentColor
    global pds
    global fixtures
    fixtures[fix] = color

    rgb = re.findall('..', color)

    r = int(rgb[0], 16)
    g = int(rgb[1], 16)
    b = int(rgb[2], 16)

    pds[int(fix)].rgb = (r,g,b)

    pds.go()

    return '',204

@app.route('/colorStream/<fix>')
def colorstream(fix):
    return Response(streamColor(fix), mimetype='text/event-stream')


@app.route('/<num>')
def test(num):
    print num
    global currentNum
    currentNum = num
    return '',204

@app.route('/current')
def current():
    print currentNum
    return str(currentNum), 202

@app.route('/stream')
def sse_request():
    return Response(
        event_stream(),
        mimetype='text/event-stream')

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)
    http_server = WSGIServer(('0.0.0.0', 80), app)
    http_server.serve_forever()
