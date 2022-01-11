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
db = client.dbsparta_plus_week4


SECRET_KEY = 'SPARTA'


# 로그인
@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['password_give']
    # pw를 암호화
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    # 해당 유저 찾기
    result = db.users.find_one({'id': id_receive, 'password': pw_hash})

    if result is not None:
        #로그인 성공시
        payload = {
            'id': id_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        # token 주기
        return jsonify({'result': 'success', 'token': token})

    else:
    #로그인 실패 시
        return jsonify({'result': 'fail', 'msg': '아이디 또는 비밀번호가 일치하지 않습니다.'})


#카드 페이지로 이동
@app.route('/')
def home2():
	token_receive = request.cookies.get('mytoken')

	try:
		payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
		print(payload)

		return render_template('mainPage.html')
	except jwt.ExpiredSignatureError:
		return redirect(url_for('login', msg='로그인 시간이 만료되었습니다.'))
	except jwt.exceptions.DecodeError:
		return redirect(url_for('login'))

#로그인 페이지로 이동
@app.route('/login')
def login():
    return render_template('login.html')

# 회원가입 경로
@app.route('/register')
def register():
    return render_template("newMemberForm.html")



if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
