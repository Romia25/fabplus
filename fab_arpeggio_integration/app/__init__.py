import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

# dealing with migration
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# a test for browsering directories
# from flask_autoindex import AutoIndex

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

# migration : naming convention
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

class MySQLAlchemy(SQLAlchemy):

    def get_tables_for_bind(self, bind=None):
        result = []
        for table in self.Model.metadata.tables.values():
            # if table.info.get('bind_key') == bind:
            if table.info.get('bind_key') == bind or (bind is not None and table.info.get('bind_key') == '__all__'):
                result.append(table)
        return result

metadata = MetaData(naming_convention=convention)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app, metadata=metadata)
# db = MySQLAlchemy(app)
# migration instance
migrate = Migrate(app, db)

appbuilder = AppBuilder(app, db.session)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from . import views
# from .modeles.save_to_db import *
# from .modeles.upload_file import * 
# from .modeles.save_to_db2 import * 
# from .modeles.save_to_db3 import *
from .view import upload_file_view, upload_file_api, list_uploaded_file
