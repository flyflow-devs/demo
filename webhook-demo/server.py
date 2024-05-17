from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json()
        print("Received JSON data:")
        pprint(data)
        return jsonify({'message': 'JSON data received and printed.'}), 200
    else:
        return jsonify({'error': 'Invalid request method.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)