from flask import Flask, render_template, request, Response
import gevent
import gevent.monkey
from gevent.pywsgi import WSGIServer
from gevent import sleep
import time
from kinet import *
import re
import json
from bss import Blu
gevent.monkey.patch_all()

app = Flask(__name__)

fixtures = {}
fixtures['fix0'] = str(000000)
fixtures['fix1'] = str(000000)
fixtures['fix2'] = str(000000)
fixtures['fix3'] = str(000000)
fixtures['fix4'] = str(000000)
fixtures['fix5'] = str(000000)

pds = PowerSupply('10.0.0.154')

x=0
while x <= 15:
    #print 'appending ' + str(x)
    pds.append(FixtureRGB(x))
    x+=3


blu = Blu("10.0.0.141")
audioControls = {}

#################
#Flask Functions#
#################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def fuckFavicon():
    return '', 204

## ColorBlast ##

@app.route('/sseColor')
def getColorStream():
    return Response(sseColorStream(), mimetype='text/event-stream')

@app.route('/setColor/<fix>/<color>')
def setColor(fix, color):
    global pds
    global fixtures
    fixtures['fix' + str(fix)] = str(color)
    rgb = re.findall('..', color)

    r = int(rgb[0], 16)
    g = int(rgb[1], 16)
    b = int(rgb[2], 16)

    pds[int(fix)].rgb = (r,g,b)
    pds.go()

    #print 'setting %s to %s' % (fix, color)
    return '', 204
#########################

## BSS Blu ##

@app.route('/sseBlu')
def getBluStream():
    return Response(sseBluStream(), mimetype='text/event-stream')

#########################
#Functions outside Flask#
#########################

## Streams ##

def sseColorStream():
    global fixtures
    lastSentData = ''
    while True:

        if str(lastSentData) != str(fixtures):
            yield 'data: %s\n\n' % json.dumps(fixtures)
            lastSentData = str(fixtures)
        gevent.sleep(0.1)

def subscribePercentage(controlName, node, vd, obj, sv):
    global audioControls

    for x in blu.subscribePercent(node, vd, obj, sv):
        audioControls[controlName] = x
        gevent.sleep(0.1)
    # Founders audio level:
    # for x in blu.subscribePercent('037E','03','000100','0000'):
    #     audioControls['Founders'] = x
    #     gevent.sleep(0.1)

gevent.spawn(subscribePercentage('Founders', '037E', '03', '000100', '0000'))
#gevent.spawn(subscribePercent('Backstage', '037E', '03', '000102', '0000'))

def sseBluStream():
    global audioControls
    lastSentData = ''

    while True:

        if str(lastSentData) != str(audioControls):
            yield 'data: %s\n\n' % json.dumps(audioControls)
            lastSentData = str(audioControls)
        gevent.sleep(0.1)


## Control Functions ##


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)
    http_server = WSGIServer(('0.0.0.0', 80), app)
    http_server.serve_forever()
