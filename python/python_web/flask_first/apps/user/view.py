import json

from flask import Blueprint, render_template, make_response, request

from apps.user.models import User
from ext import db

bp_user = Blueprint('article', __name__, template_folder='../../templates', static_folder='../../static/')


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
    id = request.args.get('id')
    user = User.query.get(id)
    print(user.article)

    article_list = list()
    for i in user.article:
        user_list = dict()
        user_list['title'] = i.title
        user_list['content'] = i.content
        user_list['save'] = i.save
        user_list['like'] = i.like
        article_list.append(user_list)
    # response = make_response(user)
    # return response
    user_dict = dict()
    user_dict['username'] = user.username
    user_dict['id'] = user.id
    user_dict['article'] = article_list
    # article_list = json.dumps(article_list)

    return user_dict
