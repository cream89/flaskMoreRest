"""
 File       : routes.py
 Time       : 2022/5/13 14:41
 Author     : 黄大彬
 version    : python 3.7.4
"""

from  flask import Blueprint
from flask_restful import  Api
from .api import *

order_blue=Blueprint('order',__name__)

api=Api(order_blue)

api.add_resource(OrderDetail,'/detail')
api.add_resource(OrderList,'/list')