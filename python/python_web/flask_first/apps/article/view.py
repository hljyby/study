from flask import Blueprint, render_template, make_response, request

from apps.article.models import Article
from apps.user.models import User

from ext import db

bp_article = Blueprint('user', __name__, template_folder='../../templates', static_folder='../../static/')


@bp_article.route('/')
def home():
    # article_list = list()
    # for i in range(3, 40):
    #     article = Article()
    #     article.title = 'title{}'.format(i)
    #     article.content = 'content{}'.format(i)
    #     article.user_id = i
    #
    #     article_list.append(article)
    # db.session.add_all(article_list)
    # db.session.commit()

    id = request.args.get('id')
    print(id)
    article = Article.query.get(id)
    print(article.user.username)
    return {'aaa': 1}
