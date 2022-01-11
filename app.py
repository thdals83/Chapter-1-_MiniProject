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
    default_card_list = list(db.cards.find({'user_email': 'bbb@naver.com', 'card_bookmark': False}))
    bookmark_card_list = list(db.cards.find({'user_email': 'bbb@naver.com', 'card_bookmark': True}))
    print(default_card_list)
    return render_template('mainPage.html', default_card_list=default_card_list, bookmark_card_list=bookmark_card_list)


# 리스트 작성 창에서 리스트 양식 값들 받아오기
@app.route('/api/pluscard', methods=['POST'])
def api_pluscard():
    # db schedule에 들어갈 정보들 dictionary 작성
    useremail = request.form['useremail']
    card_emailid = request.form['card_emailid']
    card_nameid = request.form['card_companyid']
    card_companyid = request.form['card_companyid']
    card_roleid = request.form['card_roleid']
    card_positionid = request.form['card_positionid']
    card_telid = request.form['card_telid']
    card_addressid = request.form['card_addressid']
    card_descid = request.form['card_descid']
    card_bookmarkid = request.form['card_bookmarkid']

    doc = {
        "email": useremail,
        "card_email": card_emailid,
        # 카드 이미지 추가
        "card_name": card_nameid,
        "card_company": card_companyid,
        "card_role": card_roleid,
        "card_position": card_positionid,
        "card_tel": card_telid,
        "card_address": card_addressid,
        "card_desc": card_descid,
        "card_bookmark": card_bookmarkid
    }
    print(doc)
    # db에 저장하기
    db.cards.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '등록 성공하였습니다.'})


# 명함 삭제
@app.route('/api/list', methods=["POST"])
def delete_card():
    card_id_receive = request.form['card_id_give']
    db.cards.delete_one({'_id': ObjectId(card_id_receive)})
    return jsonify({'msg': 'delete!'})


# 명함 즐겨찾기 등록 및 취소
@app.route('/api/list/bookmark', methods=["POST"])
def bookmark_card():
    card_id_receive = request.form['card_id_give']
    card = db.cards.find_one({'_id': ObjectId(card_id_receive)})

    if card['card_bookmark'] is False:
        db.cards.update_one({'_id': ObjectId(card_id_receive)}, {"$set": {'card_bookmark': True}})
        return jsonify({'msg': '즐겨찾기 등록완료'})
    else:
        db.cards.update_one({'_id': ObjectId(card_id_receive)}, {"$set": {'card_bookmark': False}})
        return jsonify({'msg': '즐겨찾기 취소'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
