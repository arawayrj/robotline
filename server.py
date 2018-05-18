import RPi.GPIO as GPIO
from flask_socketio import SocketIO, emit
from time import sleep
from flask import Flask, render_template, url_for, copy_current_request_context
from threading import Thread, Event

#stat=5

app = Flask(__name__)

socketio = SocketIO(app)
thread = Thread()
thread_stop_event = Event()

class MonitorThread(Thread):
	def __init__(self):
		self.delay = 1
		super(MonitorThread, self).__init__()
	def monitor(self):
		inPins = [5, 6, 13, 12]
		status = [0, 0, 0, 0]
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(inPins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		while not thread_stop_event.isSet():
			for pin in inPins:
				tempstat = GPIO.input(pin)
				status[inPins.index(pin)] = tempstat
			socketio.emit('newstatus', {'status': status}, namespace='/monitor')
			sleep(self.delay)
	def run(self):
		self.monitor()

@app.route('/')
def index():
	return render_template('index.html')

@socketio.on('connect', namespace='/monitor')
def test_connect():
	global thread
	if not thread.isAlive():
		thread = MonitorThread()
		thread.start()

if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', port=80)
	#app.run(debug=True, host='0.0.0.0')

