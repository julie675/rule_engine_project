from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


class FileUploadAPI(Resource):
    def post(self):  # 修正方法名和参数
        if 'file' not in request.files:  # 修正拼写
            return {'status': 'fail', 'message': 'No file part'}, 400

        file = request.files['file']  # 修正变量名
        if file.filename == '':  # 移除分号
            return {'status': 'fail', 'message': 'No selected file'}, 400

        if file and self.allowed_file(file.filename):  # 添加self.
            filename = secure_filename(file.filename)
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return {'status': 'success', 'filename': filename}, 200  # 修正引号

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS  # 修正方法名p