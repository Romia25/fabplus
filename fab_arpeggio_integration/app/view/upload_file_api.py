
import os
from flask_appbuilder import expose, ModelRestApi 
from ..modeles.upload_file import ProjectFiles
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask import request, jsonify
from .. import appbuilder
from config import UPLOAD_FOLDER
from werkzeug.utils import secure_filename


class ProjectFilesApi(ModelRestApi):
    datamodel = SQLAInterface(ProjectFiles)

    @expose('/upload', methods=['POST'])
    def upload_file(self):
        if 'file_to' not in request.files:
            respon = jsonify({'message' : 'No file part in the request'})
            return respon
        # check if there is a filename
        file_uploaded = request.files['file_to']
        if file_uploaded.filename == '' :
            responses = jsonify({'message' : 'No file selected for uploading'})
            # responses.status_code = 400
            return responses
        else :
            uploaded_filename = secure_filename(file_uploaded.filename)
            file_uploaded.save(os.path.join(UPLOAD_FOLDER, uploaded_filename))
            # file_uploaded.save(os.path.join('/home/linda/test', uploaded_filename))
            responses = jsonify({'message' : 'File  uploaded successfully'})
            return responses


appbuilder.add_api(ProjectFilesApi)
