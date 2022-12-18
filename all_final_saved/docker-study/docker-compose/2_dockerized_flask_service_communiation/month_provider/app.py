from flask import Flask, jsonify
from datetime import datetime
# import os
# from dotenv import load_dotenv


# load_dotenv('.env.custom')
# UP_API_HOST = os.environ.get('UP_API_HOST', 'localhost')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_month():
    month = datetime.now().strftime('%B')
    return jsonify({'month': month})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7103, debug=True)