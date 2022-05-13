"""
 File       : api.py
 Time       : 2022/5/13 14:41
 Author     : 黄大彬
 version    : python 3.7.4
"""

from  flask_restful import  Resource


class  OrderList(Resource):

    def  get(self):

        return 'order  list'




class OrderDetail(Resource):

    def  get(self):

        return 'order detail'
