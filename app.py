from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 初始化Flask应用
app = Flask(__name__)

# 配置SQLite数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 定义用户表模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# 定义规则表模型
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    condition = db.Column(db.String(200), nullable=False)

# 定义结果表模型
class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rule_id = db.Column(db.Integer, db.ForeignKey('rule.id'))
    status = db.Column(db.String(20))

# 基础路由
@app.route('/')
def home():
    return "Hello World!"

# 启动应用
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 创建所有数据表
    app.run(debug=True)

from flask import Flask
from flask_restful import Api
from auth import LoginAPI
from upload import FileUploadAPI
from results import ResultAPI

app = Flask(__name__)
api = Api(app)

# 配置上传文件夹
app.config['UPLOAD_FOLDER'] = 'uploads'

# 注册API路由
api.add_resource(LoginAPI, '/api/login')
api.add_resource(FileUploadAPI, '/api/upload')
api.add_resource(ResultAPI, '/api/results')

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # 允许外部访问
        port=5000,       # 端口号
        debug=True,      # 调试模式（自动重载代码）
        threaded=True    # 多线程处理请求
    )