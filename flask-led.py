from gpiozero import LED
from time import sleep
from flask import Flask, render_template, request, jsonify

# declare leds
red = LED(17)

# start Flask server
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('interface.html')

@app.route('/ip')
def ip():
    return jsonify({'ip': request.remote_addr, 'status': 200})

@app.route('/led/status')
def ledStatus():
    return jsonify({'isLit': red.is_lit, 'status': 200})
    
@app.route('/led/on')
def putOnLedPleaz():
    red.on()
    return jsonify({'message': 'Thankyou come again', 'status': 200})

@app.route('/led/off')
def putOffLedPleaz():
    red.off()
    return jsonify({'message': 'Lights are out', 'status': 200})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
