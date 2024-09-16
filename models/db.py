from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey