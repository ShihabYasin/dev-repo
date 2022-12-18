from flask import Flask, request, jsonify, make_response
import requests
# import os
# from dotenv import load_dotenv


# load_dotenv('.env.custom')
# UP_API_HOST = os.environ.get('UP_API_HOST', 'localhost')


app = Flask(__name__)

@app.route('/day', methods=['GET'])
def get_day_data():
    response = {'error': 'invalid value'}
    response = requests.get(f'''http://day_provider:7102/''').json()
    return make_response(jsonify(response), 200)

@app.route('/month', methods=['GET'])
def get_month_data():
    response = {"data": ""}
    response = requests.get(f'''http://month_provider:7103/''').json()
    return make_response(jsonify(response), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7101, debug=True)