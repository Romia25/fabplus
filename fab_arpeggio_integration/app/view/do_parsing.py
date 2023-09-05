from flask import jsonify
from pathlib import Path
from config import UPLOAD_FOLDER
from arpeggio import ParserPython, visit_parse_tree
from arpeggios.doc_things.line.csv_grammar_line import *
from arpeggios.doc_things.line.csv_visitor import *

class DoParsing():

    init_directory = Path(UPLOAD_FOLDER)

#  @expose('parsess', methods=['POST'])
    def parse_and_save(self):
        
        # if 'file_parsing' not in request.form:
        #     resp = jsonify({'Message' : 'You must select a file to parse'})
        #     return resp
        
        file_to_parse = self.get_filename() #request.form['file_parsing']
        if file_to_parse != '' and Path(file_to_parse).is_file:

            # to_be_parse_filename = secure_filename(file_to_parse)
            to_be_parse_filename = self.init_directory.joinpath(file_to_parse)

            file_content = open(to_be_parse_filename, 'r').read()

            parser = ParserPython(csv, ws='\t', debug=True)

            parse_tree_data = parser.parse(file_content)

            result = visit_parse_tree(parse_tree_data, CsvVisitor())

            parsed_file = Path('/home/linda/Documents').joinpath(file_to_parse)

           
            resp2 = jsonify({'Message' : 'Parsing is successfull!!!'})
            return resp2
        
        return jsonify({'Message' : 'Fail to parse the file'})
