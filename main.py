from flask import Flask, render_template, request, Response
import gevent
import gevent.monkey
from gevent.pywsgi import WSGIServer
from gevent import sleep
import time
from kinet import *
import re
import json
gevent.monkey.patch_all()

app = Flask(__name__)

events = {}
events['fix0'] = str(000000)
events['fix1'] = str(000000)
events['fix2'] = str(000000)
events['fix3'] = str(000000)
events['fix4'] = str(000000)
events['fix5'] = str(000000)

pds = PowerSupply('10.0.0.154')

x=0
while x <= 15:
    #print 'appending ' + str(x)
    pds.append(FixtureRGB(x))
    x+=3

#################
#Flask Functions#
#################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def fuckFavicon():
    return '', 204

@app.route('/sseColor')
def getStream():
    return Response(sseColorStream(), mimetype='text/event-stream')

@app.route('/setColor/<fix>/<color>')
def setColor(fix, color):
    global pds
    global events
    events['fix' + str(fix)] = str(color)
    rgb = re.findall('..', color)

    r = int(rgb[0], 16)
    g = int(rgb[1], 16)
    b = int(rgb[2], 16)

    pds[int(fix)].rgb = (r,g,b)
    pds.go()

    #print 'setting %s to %s' % (fix, color)
    return '', 204


#########################
#Functions outside Flask#
#########################

## Streams ##

def sseColorStream():

    global events
    lastSentData = ''

    while True:

        if str(lastSentData) != str(events):
            yield 'data: %s\n\n' % json.dumps(events)
            lastSentData = str(events)
        gevent.sleep(0.1)

## Control Functions ##



if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)
    http_server = WSGIServer(('0.0.0.0', 80), app)
    http_server.serve_forever()





