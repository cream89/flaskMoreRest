"""
 File       : app.py
 Time       : 2022/5/13 14:47
 Author     : 黄大彬
 version    : python 3.7.4
"""
from flask import  Flask

from exts.db import db
from config.settings import setting
from apps.order.routes import order_blue
from apps.user.routes import user_blue

def  create_app():

    app=Flask(__name__)
    app.config.from_object(setting)
    db.init_app(app)
    app.register_blueprint(user_blue,url_prefix='/system')
    app.register_blueprint(order_blue, url_prefix='/order')
    return app





