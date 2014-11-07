from flask import Flask, render_template, request, Response
import gevent
import gevent.monkey
from gevent.pywsgi import WSGIServer
from gevent import sleep
import time
from kinet import *
import re
gevent.monkey.patch_all()

app = Flask(__name__)

data = ''

events = {}
events['fix0'] = 000000
events['fix1'] = 000000
events['fix2'] = 000000
events['fix3'] = 000000
events['fix4'] = 000000
events['fix5'] = 000000

#################
#Flask Functions#
#################

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/favicon.ico')
def fuckFavicon():
	return '', 204

@app.route('/sse')
def getStream():
	return Response(sseStream(), mimetype='text/event-stream')

@app.route('/setColor/<fix>/<color>')
def setColor(fix, color):
	#events['fix' + str(fix)] = color
	data = 'event: fix%s\n data: %s\n\n' % (fix, color)
	print 'setting %s to %s' % (fix, color)
	return '', 204


#########################
#Functions outside Flask#
#########################

def sseStream():
	global data
	lastSentData = 'event: null\n data: null\n\n'

	while True:
		if str(lastSentData) != str(data):
			yield data
			lastSentData = data
		gevent.sleep(0.1)

# def sseStream(event):
# 	global events
# 	lastSentData = ''

# 	while True:

# 		if str(lastSentData) != str(events[event]):
# 			yield 'data: %s\n\n' % (events[event])
# 			lastSentData = events[event]

# 		gevent.sleep(0.1)

#########################

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)
    http_server = WSGIServer(('0.0.0.0', 80), app)
    http_server.serve_forever()
