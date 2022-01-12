from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.dbsparta_plus_week4

# JWT 비밀문자열
SECRET_KEY = 'SPARTA'


# JWT 패키지
import jwt

# 토큰에 만료시간
import datetime

# 회원가입 시, 비밀번호를 암호화
import hashlib






#카드 페이지로 이동
@app.route('/index')
def home2():
    return render_template('mainPage.html')


#로그인 페이지로 이동
@app.route('/login')
def login():
    return render_template('login.html')


# 회원가입 경로
@app.route('/register')
def register():
    return render_template("newMemberForm.html")


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
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        # token 주기
        return jsonify({'result': 'success', 'token': token})

    # 로그인 실패 시
    else:
        return jsonify({'result': 'fail', 'msg': '아이디 또는 비밀번호가 일치하지 않습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
