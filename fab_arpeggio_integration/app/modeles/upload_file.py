from flask_appbuilder import Model
from flask_appbuilder.filemanager import get_file_original_name
from sqlalchemy import Column, ForeignKey, INTEGER, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship
from flask_appbuilder.models.mixins import FileColumn, AuditMixin
from .. import db
from datetime import datetime


# class Project(Model):
#     id = Column(INTEGER, primary_key = True)
#     name = Column(String(50), unique = True, nullable=False)

class ProjectFiles(Model, AuditMixin):
    id = Column(INTEGER, primary_key = True)
    # project_id = Column(INTEGER, ForeignKey(Project.id))
    # project = relationship("Project")
    file = Column(FileColumn, nullable = False)
    description = Column(String(100))

    def get_file_name(self):
        return get_file_original_name(str(self.file))


# After parsing we have to save parsed data into db
# down there we're going to create a object corresponding 
# to the database element, we're going to process
# right now it' a csv
# class CSVSave(Model):
#     __bind_key__ = 'DB2'
#     id = Column(INTEGER, primary_key=True)
#     csv_content = Column(String())
#     filename = Column(String(150))
#     created_at = Column(TIMESTAMP, default=datetime.now())
#     updated_at = Column(TIMESTAMP, onupdate=datetime.now())

#     # create a CSVSave object
#     def __init__(self, csv_cont, name):
#         self.csv_content = csv_cont
#         self.filename = name
    
#     # save into db : perform an insert
#     @staticmethod
#     def insert_create(csv_cont, name):
#         csvel = CSVSave(csv_cont, name)
#         db.session.add(csvel)
#         db.session.commit()

# class CSVSave2(Model):
#     id = Column(INTEGER, primary_key=True)
#     csv_content_col1 = Column(String())
#     csv_content_col2 = Column(String())
#     csv_content_col3 = Column(String())
#     csv_content_col4 = Column(String())
#     csv_content_col5 = Column(String())
#     filename = Column(String(150))
#     created_at = Column(TIMESTAMP, default=datetime.now())
#     updated_at = Column(TIMESTAMP, onupdate=datetime.now())

#     # create a CSVSave object
#     def __init__(self, csv_cont1, csv_cont2, csv_cont3,
#                  csv_cont4, csv_cont5, name):
#         self.csv_content_col1 = csv_cont1
#         self.csv_content_col2 = csv_cont2
#         self.csv_content_col3 = csv_cont3
#         self.csv_content_col4 = csv_cont4
#         self.csv_content_col5 = csv_cont5
#         self.filename = name
    
#     # save into db : perform an insert
#     @staticmethod
#     def insert_create2(csv_cont1, csv_cont2, csv_cont3,
#                  csv_cont4, csv_cont5, name):
#         csvel2 = CSVSave2(csv_cont1, csv_cont2, csv_cont3,
#                  csv_cont4, csv_cont5, name)
#         db.session.add(csvel2)
#         db.session.commit()


# #################################################################################
# ####Down there goes table structure of hot and cat file
# ###############################################################################


