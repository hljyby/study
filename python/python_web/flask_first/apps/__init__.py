from flask import Flask
import settings
from apps.user.view import bp_user
from apps.article.view import bp_article
from apps.goods.view import bp_goods

from ext import db


def create_app(name):
    app = Flask(name)
    app.config.from_object(settings.DevelopmentConfig())
    db.init_app(app)
    app.register_blueprint(bp_user, url_prefix='/user')
    app.register_blueprint(bp_article, url_prefix='/article')
    app.register_blueprint(bp_goods, url_prefix='/goods')

    # print(app.url_map)
    return app
