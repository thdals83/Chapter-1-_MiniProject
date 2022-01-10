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
    return render_template('index.html')

@app.route('/newMember', methods=['POST'])
def post_new_member():
    email1 = request.form['email1']
    email2 = request.form['email2']
    email = email1+'@'+email2
    name = request.form['name']
    password1 = request.form['password1']
    password2 = request.form['password2']
    company = request.form['company']
    role = request.form['role']
    position = request.form['position']
    tel = request.form['tel']
    address = request.form['address']

    if email1 == "" or email2 == "" or name == "" or password1 == "" or password2 == "" or company == "" or role == "":
        return jsonify({'msg': '필수 입력 사항을 확인 하세요'})

    emails = list(db.users.find({'email': email}, {'_id': False}))
    is_validate_email = False

    if(len(emails) == 0):
        is_validate_email = True
    else:
        return jsonify({'msg': '유효하지 않은 이메일'})

    if is_validate_email and (password1 == password2):
        doc = {'email': email, 'name': name, 'password': password1,
               'company': company, 'role': role, 'position': position, 'tel': tel, 'address': address}
        db.users.insert_one(doc)

    if is_validate_email and (password1 != password2):
        return jsonify({'msg': '비밀번호를 학인해 주세요'})

    return jsonify({'msg': '회원가입 완료'})

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    emails = list(db.users.find({'email': email}, {'_id': False}))
    is_validate = False
    if(len(emails) == 0):
        is_validate = True
    return jsonify({'validate': is_validate})


@app.route('/new_member_form')
def new_member_form():
    return render_template('newMemberForm.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
