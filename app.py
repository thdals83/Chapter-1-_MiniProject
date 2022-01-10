import hashlib

from bson.json_util import dumps
from operator import itemgetter
import jwt
from bson import ObjectId
from pymongo import MongoClient
from datetime import datetime, timedelta
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.card

SECRET_KEY = 'SPARTA'


@app.route('/')
def home():
    return render_template('mainPage.html')


# @app.route('/api/list', methods="GET")
# def get_card_list():
    # card_list = list(db.cards.find({'user_email': }))
    # img = request.args.get('')
    # return print('asdlkfjhads')


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
