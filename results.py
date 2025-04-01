from flask_restful import Resource, reqparse
import sqlite3


class ResultAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('user_id', type=int, required=True)

    def get(self):
        args = self.parser.parse_args()
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM results WHERE user_id=?", (args['user_id'],))
        results = cursor.fetchall()
        conn.close()

        return {
            'status': 'success',
            'data': [dict(zip(['id', 'user_id', 'result', 'timestamp'], row)) for row in results]
        }, 200