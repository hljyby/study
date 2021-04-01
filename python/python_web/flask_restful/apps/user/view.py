from flask_restful import Resource, marshal_with, fields, reqparse, inputs
from flask import Blueprint
from werkzeug.datastructures import FileStorage
from flask_restful import Api

from apps.user.model import User

user_bp = Blueprint('user', __name__)
api = Api(user_bp)

user_field = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'created': fields.DateTime,

}
# bundle_errors=True 如果有错全部提示出来，如果不写只会报一个错
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('username', type=str, required=True, help='必须输入用户名')
# parser.add_argument('username', type=str, require=True, help='必须输入用户名', location=['form']) # 必须在form中添加 在params 中添加不好使 限制必须是post 请求
parser.add_argument('password', type=inputs.regex(r'/^[0-9]+$/'), help='必须输入密码')
# parser.add_argument('name', action='append', help='必须输入密码')  # 允许多个字段存在
# parser.add_argument('name', dest='public_name')  # 允许多个字段存在
# location 后面可以跟 form args headers cookies uploads
# parser.add_argument(type=list, location=['json', 'args'])
parser.add_argument('picture', type=FileStorage, location=['files'])


class UserResource(Resource):
    @marshal_with(user_field)
    def get(self):
        users = User.query.all()

        return users

    def post(self):
        args = parser.parse_args()
        username = args.get('username')
        # public_name = args['public_name']
        picture = args.get('picture')
        print(picture.filename)
        picture.save(picture.filename)
        return {'msg': '======>post'}

    def put(self):
        pass

    def delete(self):
        pass


api.add_resource(UserResource, '/UserResource')
