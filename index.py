from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

LED1 = 23
LED2 = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/led1/on")
def led1_on():
	try:
		GPIO.output(LED1, GPIO.HIGH)
		return "ok"
	except Exception as e:
		return f"fail: {str(e)}"

@app.route("/led1/off")
def led1_off():
	try:
		GPIO.output(LED1, GPIO.LOW)
		return "ok"
	except Exception as e:
		return f"fail: {str(e)}"

@app.route("/led2/on")
def led2_on():
	try:
		GPIO.output(LED2, GPIO.HIGH)
		return "ok"
	except Exception as e:
		return f"fail: {str(e)}"

@app.route("/led2/off")
def led2_off():
	try:
		GPIO.output(LED2, GPIO.LOW)
		return "ok"
	except Exception as e:
		return f"fail: {str(e)}"

@app.route("/shutdown")
def shutdown():
	GPIO.cleanup()  # GPIO 설정 해제
	return "GPIO cleaned up, server shutting down."

if __name__ == "__main__":
	try:
		app.run(host="0.0.0.0")
	except KeyboardInterrupt:
		GPIO.cleanup()  # GPIO 설정 해제
