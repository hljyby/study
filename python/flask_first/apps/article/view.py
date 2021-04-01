from flask import Blueprint, render_template, make_response, request

from apps.user.models import User
from ext import db

bp_user = Blueprint('user', __name__, template_folder='../../templates', static_folder='../../static/')


@bp_user.route('/')
def home():
    # user_list = list()
    # for i in range(1, 40):
    #     user = User()
    #     user.username = 'yby{}'.format(i)
    #     user_list.append(user)
    # db.session.add_all(user_list)
    # db.session.commit()
    # return render_template('/users/test.html')
    user = User.query.filter(User.id.__lt__(10)).first()
    print(user.username)
    response = make_response(user)
    return response
