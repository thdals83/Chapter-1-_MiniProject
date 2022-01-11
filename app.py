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
    default_card_list = list(db.cards.find({'email': 'bbb@naver.com', 'card_bookmark': 0}))
    bookmark_card_list = list(db.cards.find({'email': 'bbb@naver.com', 'card_bookmark': 1}))
    # print(bookmark_card_list)

    return render_template('mainPage.html', default_card_list=default_card_list, bookmark_card_list=bookmark_card_list)


def get_word(select_word, input_word, bookmark):
    return list(db.cards.find({'email': 'bbb@naver.com', select_word: {'$regex': input_word}, 'card_bookmark': bookmark}))


@app.route('/api/search', methods=['POST'])
def api_search():
    select_receive = request.form['select_give']
    input_receive = request.form['input_give']

    if select_receive == 'company':
        search_list = get_word('card_company', input_receive, 0)
        return jsonify({'result': dumps(search_list)})
    elif select_receive == 'name':
        search_list = get_word('card_name', input_receive, 0)
        return jsonify({'result': dumps(search_list)})
    elif select_receive == 'position':
        search_list = get_word('card_position', input_receive, 0)
        return jsonify({'result': dumps(search_list)})
    elif select_receive == 'role':
        search_list = get_word('card_role', input_receive, 0)
        return jsonify({'result': dumps(search_list)})
    elif select_receive == 'tel':
        search_list = get_word('card_tel', input_receive, 0)
        return jsonify({'result': dumps(search_list)})
    elif select_receive == 'email':
        search_list = get_word('card_email', input_receive, 0)
        return jsonify({'result': dumps(search_list)})


@app.route('/api/search/bookmark', methods=['POST'])
def api_search_bookmark():
    select_receive = request.form['select_give']
    input_receive = request.form['input_give']

    if select_receive == 'company':
        search_list = get_word('card_company', input_receive, 1)
        return jsonify({'result': dumps(search_list)})
    elif select_receive == 'name':
        search_list = get_word('card_name', input_receive, 1)
        return jsonify({'result': dumps(search_list)})
    elif select_receive == 'position':
        search_list = get_word('card_position', input_receive, 1)
        return jsonify({'result': dumps(search_list)})
    elif select_receive == 'role':
        search_list = get_word('card_role', input_receive, 1)
        return jsonify({'result': dumps(search_list)})
    elif select_receive == 'tel':
        search_list = get_word('card_tel', input_receive, 1)
        return jsonify({'result': dumps(search_list)})
    elif select_receive == 'email':
        search_list = get_word('card_email', input_receive, 1)
        return jsonify({'result': dumps(search_list)})


@app.route('/api/sort', methods=['POST'])
def api_sort():
    default_list_action_receive = request.form['default_list_action_give']

    default_list = list(db.cards.find({'email': 'bbb@naver.com', 'card_bookmark': 0}))

    if default_list_action_receive == 'register':
        return jsonify({'result': dumps(default_list)})
    elif default_list_action_receive == 'company':
        default_list = sorted(default_list, key=itemgetter('card_company'))
        return jsonify({'result': dumps(default_list)})
    elif default_list_action_receive == 'name':
        default_list = sorted(default_list, key=itemgetter('card_name'))
        return jsonify({'result': dumps(default_list)})


@app.route('/api/sort/bookmark', methods=['POST'])
def api_sort_bookmark():
    bookmark_list_action_receive = request.form['bookmark_list_action_give']

    bookmark_list = list(db.cards.find({'email': 'bbb@naver.com', 'card_bookmark': 1}))

    if bookmark_list_action_receive == 'register':
        return jsonify({'result': dumps(bookmark_list)})
    elif bookmark_list_action_receive == 'company':
        bookmark_list = sorted(bookmark_list, key=itemgetter('card_company'))
        return jsonify({'result': dumps(bookmark_list)})
    elif bookmark_list_action_receive == 'name':
        bookmark_list = sorted(bookmark_list, key=itemgetter('card_name'))
        return jsonify({'result': dumps(bookmark_list)})


# 리스트 작성 창에서 리스트 양식 값들 받아오기
@app.route('/api/pluscard', methods=['POST'])
def api_pluscard():
    # db schedule에 들어갈 정보들 dictionary 작성
    useremail = request.form['useremail']
    card_emailid = request.form['card_emailid']
    card_nameid = request.form['card_nameid']
    card_companyid = request.form['card_companyid']
    card_roleid = request.form['card_roleid']
    card_positionid = request.form['card_positionid']
    card_telid = request.form['card_telid']
    card_addressid = request.form['card_addressid']
    card_descid = request.form['card_descid']
    card_bookmarkid = int(request.form['card_bookmarkid'])

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
        "card_bookmark": card_bookmarkid,

        "register_time": datetime.now().timestamp()
    }
    print(doc)
    # db에 저장하기
    db.cards.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '등록 성공하였습니다.'})


# 명함 삭제
@app.route('/api/list/delete', methods=["POST"])
def delete_card():
    card_id_receive = request.form['card_id_give']
    db.cards.delete_one({'_id': ObjectId(card_id_receive)})
    return jsonify({'msg': 'delete!'})


# 명함 즐겨찾기 등록 및 취소
@app.route('/api/list/bookmark', methods=["POST"])
def bookmark_card():
    card_id_receive = request.form['card_id_give']
    card = db.cards.find_one({'_id': ObjectId(card_id_receive)})

    if card['card_bookmark'] is 0:
        db.cards.update_one({'_id': ObjectId(card_id_receive)}, {"$set": {'card_bookmark': 1}})
        return jsonify({'msg': '즐겨찾기 등록완료'})
    else:
        db.cards.update_one({'_id': ObjectId(card_id_receive)}, {"$set": {'card_bookmark': 0}})
        return jsonify({'msg': '즐겨찾기 취소'})
    # return jsonify({'result': user})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
