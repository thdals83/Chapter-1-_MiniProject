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
    return render_template('mainPage.html', default_card_list=default_card_list, bookmark_card_list=bookmark_card_list)


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
    card_bookmarkid = int(request.form['card_bookmarkid'])

    file = request.files['file']
    extension = file.filename.split('.')
    today = datetime.now()
    mytime = today.strftime('%Y년%m월%d일%H:%M:%S')
    filename = f'{mytime}-{extension[0]}'
    filename = "".join(i for i in filename if i not in "\/:*?<>|")
    filename = filename.strip()
    save_to = f'static/images/{filename}.{extension[1]}.jpg'
    file.save(save_to)

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
        "imgurl": f'{filename}.{extension[1]}.jpg'
    }
    # db에 저장하기
    db.cards.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '등록 성공하였습니다.'})

@app.route('/api/editcard', methods=['POST'])
def api_editcard():
    use_card_nameid = request.form['use_card_nameid']
    use_card_emailid = request.form['use_card_emailid']
    use_card_telid = request.form['use_card_telid']
    use_card_companyid = request.form['use_card_companyid']
    use_card_roleid = request.form['use_card_roleid']
    use_card_positionid = request.form['use_card_positionid']
    use_card_addressid = request.form['use_card_addressid']
    use_card_descid = request.form['use_card_descid']

    hide_id = request.form['hide_id']

    file = request.files['file']
    extension = file.filename.split('.')
    today = datetime.now()
    mytime = today.strftime('%Y년%m월%d일%H:%M:%S')
    filename = f'{mytime}-{extension[0]}'
    filename = "".join(i for i in filename if i not in "\/:*?<>|")
    filename = filename.strip()
    save_to = f'static/images/{filename}.{extension[1]}.jpg'
    file.save(save_to)

    doc = {
        "card_email": use_card_emailid,
        # 카드 이미지 추가
        "card_name": use_card_nameid,
        "card_company": use_card_companyid,
        "card_role": use_card_roleid,
        "card_position": use_card_positionid,
        "card_tel": use_card_telid,
        "card_address": use_card_addressid,
        "card_desc": use_card_descid,
        "imgurl": f'{filename}.{extension[1]}.jpg',
    }
    # db에 저장하기
    db.cards.update_one({'_id':ObjectId(hide_id)}, {'$set':doc})
    return jsonify({'result': 'success', 'msg': ' 수정 성공하였습니다.'})


# 명함 삭제
@app.route('/api/list', methods=["POST"])
def delete_card():
    card_id_receive = request.form['card_id_give']
    db.cards.delete_one({'_id': ObjectId(card_id_receive)})
    return jsonify({'msg': 'delete!'})

# 명함 찾기
@app.route('/api/getcard', methods=["POST"])
def get_card():
    getcard_id = request.form['getcard_id']
    cardinfo =  list(db.cards.find({'_id': ObjectId(getcard_id)}))
    cardinfo[0]['_id'] = str(cardinfo[0]['_id'])
    return jsonify({'cardinfo': cardinfo})

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


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
