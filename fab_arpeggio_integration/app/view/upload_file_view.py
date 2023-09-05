from flask_appbuilder.models.sqla.interface import SQLAInterface
from .. import appbuilder, db
from flask_appbuilder import ModelView, expose
# from arpeggios.doc_things.line.csv_parsing_test import restat, filename

from ..modeles.upload_file import *


# class ProjectView(ModelView):
#     project_data = SQLAInterface(Project)

# def parsing_csv():

#         return response(201 , message = "je suis une linda")

class ProjectFilesView(ModelView):
    datamodel = SQLAInterface(ProjectFiles)

    label_columns = {'get_file_name' : 'Filename'}
    show_columns = ['get_file_name']

    # @expose('/parsing')
    # def parsing_csv(self):

    #     for child in restat:

    #         CSVSave.insert_create(child, filename)

    #     return restat 


appbuilder.add_view(ProjectFilesView, "Files to be uploaded", category='Files')
# appbuilder.add_link('Parsing_csv', href="/projectfilesview/parsing", category='Parsi')

# appbuilder.
db.create_all()