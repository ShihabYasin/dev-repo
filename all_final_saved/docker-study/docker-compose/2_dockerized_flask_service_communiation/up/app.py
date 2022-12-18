from flask import Flask, request, jsonify, make_response
import requests
# import os
# from dotenv import load_dotenv


# load_dotenv('.env.custom')
# UP_API_HOST = os.environ.get('UP_API_HOST', 'collect')


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    data = request.json['data']    
    response = {'error': 'invalid value'}
    if data == 'day':
        response = requests.get(f'''http://collect:7101/day''').json()        
    elif data == 'month':
        response = requests.get(f'''http://collect:7101/month''').json() 
    return make_response(jsonify(response), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7100, debug=True)