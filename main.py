from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.get_json()
    print("Received data from Minecraft mod:", data)
    # Process the data as needed
    return {'status': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
