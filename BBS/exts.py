# exts.py
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate
from flask_mail import Mail
from utils.alidayu import AlidayuAPI

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
se = Session()
alidayu = AlidayuAPI()


def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    se.init_app(app=app)
    mail.init_app(app=app)
    alidayu.init_app(app=app)

