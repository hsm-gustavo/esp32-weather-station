from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app, resources={r"/data": {"origins": "*"}})

@app.route('/data', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type'])
def receive_data() -> Response:
    global temperature
    global humidity
    if request.method == 'POST':
        data = request.get_json()
        if 'temperature' in data and 'humidity' in data:
            temperature = data['temperature']
            humidity = data['humidity']
            print(f"Humidity: {humidity:.2f}% Temperature: {temperature:.2f}°C")
            return jsonify({'message': 'Data received successfully'}), 200
        else:
            return jsonify({'error': 'Invalid data format'}), 400
        
    elif request.method == 'GET':
        return jsonify({'temperature': temperature, 'humidity': humidity}), 200
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
