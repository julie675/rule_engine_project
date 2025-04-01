from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash


class LoginAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True)
        self.parser.add_argument('password', type=str, required=True)

    def post(self):
        args = self.parser.parse_args()
        # 这里应该查询数据库验证用户
        user = get_user_from_db(args['username'])  # 需要实现这个函数
        if user and check_password_hash(user.password, args['password']):
            return {'status': 'success', 'token': 'generated_token'}, 200
        return {'status': 'fail', 'message': 'Invalid credentials'}, 401

import sqlite3

def get_user_from_db(username: str):
    """从数据库查询用户信息"""
    conn = sqlite3.connect('rules.db')  # 确保与您的数据库文件名一致
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()  # 返回 (id, username, password) 或 None
    conn.close()
    return user