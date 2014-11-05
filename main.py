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

fixtures ={'fix1':'0', 'fix2':'0', 'fix3':'0', 'fix4':'0', 'fix5':'0'}

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



def streamColor():
    global currentColor
    print currentColor
    lastColor = ''
    while True:
        if lastColor != currentColor:
            print currentColor
            yield 'data: %s\n\n' % currentColor
            lastColor = currentColor
        gevent.sleep(0.1)


@app.route('/setColor/<color>')
def setColor(color):
    global currentColor
    currentColor = color
    color = re.findall('..', color)
    r = int(color[0], 16)
    g = int(color[1], 16)
    b = int(color[2], 16)
    global pds
    pds[0].rgb = (r,g,b)
    pds.go()

    return '',204

@app.route('/colorStream')
def colorstream():
    return Response(streamColor(), mimetype='text/event-stream')


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
