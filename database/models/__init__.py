from ..connect import db

from .users import Users

db.create_tables([Users])
