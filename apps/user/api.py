"""
 File       : api.py
 Time       : 2022/5/13 14:41
 Author     : 黄大彬
 version    : python 3.7.4
"""


from  flask_restful import  Resource


class  User(Resource):

    def  get(self):

        return 'user  list'




class Role(Resource):

    def  get(self):

        return 'role list'
