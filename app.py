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

# db.users.insert_one({
#     'email': 'aaa@naver.com',
#     'name': '홍길동',
# })

# db.cards.insert_many([
#     {
#         'user_email': 'bbb@naver.com',
#         'card_name': '김두한',
#         'card_bookmark': True,
#     },
#     {
#         'user_email': 'bbb@naver.com',
#         'card_name': '고두심',
#         'card_bookmark': False,
#     },
#     {
#         'user_email': 'bbb@naver.com',
#         'card_name': '홍길동',
#         'card_bookmark': False,
#     },
#     {
#         'user_email': 'bbb@naver.com',
#         'card_name': '나나나',
#         'card_bookmark': False,
#     },
# ])


@app.route('/')
def home():
    default_card_list = list(db.cards.find({'user_email': 'bbb@naver.com', 'card_bookmark': False}))
    bookmark_card_list = list(db.cards.find({'user_email': 'bbb@naver.com', 'card_bookmark': True}))
    print(default_card_list)
    return render_template('mainPage.html', default_card_list=default_card_list, bookmark_card_list=bookmark_card_list)


# @app.route('/api/list', methods=["GET"])
# def get_card_list():
#     return jsonify(card_list)


# 명함 삭제
@app.route('/api/list', methods=["POST"])
def delete_card():
    card_id_receive = request.form['card_id_give']
    db.cards.delete_one({'_id': ObjectId(card_id_receive)})
    return jsonify({'msg': 'delete!'})


@app.route('/api/list/bookmark', methods=["POST"])
def bookmark_card():
    card_id_receive = request.form['card_id_give']
    bookmark_receive = bool(request.form['bookmark_give'])
    card = db.cards.find_one({'user_email': 'bbb@naver.com'})
    card_list = db.cards.update_one({'_id': ObjectId(card_id_receive)})

    if bookmark_receive is True:
        db.cards.update_one({'_id': ObjectId(card_id_receive)}, {"$set": {'card_bookmark': True}})
        return jsonify({'msg': '즐겨찾기 등록완료'})
    else:
        db.cards.update_one({'_id': ObjectId(card_id_receive)}, {"$set": {'card_bookmark': False}})
        return jsonify({'msg': '즐겨찾기 취소'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
