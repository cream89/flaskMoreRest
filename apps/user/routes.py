"""
 File       : routes.py
 Time       : 2022/5/13 14:41
 Author     : 黄大彬
 version    : python 3.7.4
"""

from flask_restful import Api
from flask import  Blueprint
from .api import *


user_blue=Blueprint('user',__name__)

api=Api(user_blue)

api.add_resource(User,'/user')
api.add_resource(Role,'/role')

