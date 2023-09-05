from .. import appbuilder
from pathlib import Path
from shutil import move
from config import UPLOAD_FOLDER
from flask_appbuilder import expose, BaseView
from datetime import datetime
from werkzeug.utils import secure_filename #safe_join
from flask import abort , render_template, \
    request, jsonify
from arpeggio import ParserPython, visit_parse_tree
from arpeggios.doc_things.line.csv_grammar_line import *
from arpeggios.doc_things.line.csv_visitor import *
# from .upload_file_view import parsing_csv

class ListDirectory(BaseView):

    # we create a variable we'll use for listing the UPLOAD_FOLDER
    init_directory = Path(UPLOAD_FOLDER)
    move_folder = init_directory.parent

    # convert a float datetime to yyyy-mm-dd hh:mm:ss fromat
    def convert_datetime(self, DateTime):
        dt = datetime.utcfromtimestamp(DateTime)
        formated_datetime = dt.strftime('%Y-%m-%d %H:%M:%S')
        return formated_datetime
    
    #get file to be parsed (filename) and send it to method that will do parsing
    # as well as visitor so that we get filename inserted into db
    # @expose('getfilename', methods=['POST'])
    # def get_filename(self):
    #     if 'file_parsing' not in request.form:
    #         resp = jsonify({'Message' : 'You must select a file to parse'})
    #         return resp
        
    #     file_to_parse = request.form['file_parsing']

    #     return file_to_parse

    # execute the parsing
    @expose('parsess', methods=['POST'])
    def parse_and_save(self):
        
        if 'file_parsing' not in request.form:
            resp = jsonify({'Message' : 'You must select a file to parse'})
            return resp
        
        file_to_parse = request.form['file_parsing']
        if file_to_parse != '' and Path(file_to_parse).is_file:

            # to_be_parse_filename = secure_filename(file_to_parse)
            to_be_parse_filename = self.init_directory.joinpath(file_to_parse)

            file_content = open(to_be_parse_filename, 'r').read()

            csv_vis = CsvVisitor()
            csv_vis.filename = file_to_parse

            parser = ParserPython(csv, ws='\t', debug=True)

            parse_tree_data = parser.parse(file_content)

            result = visit_parse_tree(parse_tree_data, csv_vis)

           
            resp2 = jsonify({'Message' : 'Parsing is successfull!!!'})
            # parsed_file = Path('/home/linda/Documents').joinpath(file_to_parse)
            # moved successfully parsed files into a different directory
            move(str(to_be_parse_filename), str(self.move_folder))
            return  result
        
        
        
        return jsonify({'Message' : 'Fail to parse the file'})

    # a method for listing content of upload directory
    @expose('/listfiles')
    def list_directory(self):
        
        if not self.init_directory.exists():
            return abort(404, message="Directory doesn't exist !!!")

        # show the directory content
        path_object_iter = self.init_directory.iterdir()

        files_and_dir = [
            {
                'filename' : file.name,
                'file_last_modified' : self.convert_datetime(file.stat().st_mtime)     
            } for file in path_object_iter
        ]

        return render_template(
            'folder_content.html', appbuilder=appbuilder, 
            files=files_and_dir
        )



appbuilder.add_view(ListDirectory, "List Directory", 
    href='/listdirectory/listfiles', icon='fa-folder', category='Uploaded Files'
    )

