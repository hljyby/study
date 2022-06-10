from flask import Blueprint, render_template, make_response, request

from apps.article.models import *
from apps.user.models import *
from apps.goods.models import *

from ext import db

bp_goods = Blueprint('goods', __name__, template_folder='../../templates', static_folder='../../static/')


@bp_goods.route('/')
def home():
    # goods_list = list()
    # user_goods_list = list()
    # for i in range(3, 40):
    # goods = Goods()
    # goods.gname = 'Goods{}'.format(i)
    # goods.price = i
    # goods_list.append(goods)
    # user_goods_list.append(user_goods)
    # db.session.add_all(goods_list)
    # db.session.add_all(user_goods_list)

    # db.session.commit()

    id = request.args.get('id')
    print(id)
    ug = User_goods.query.filter(User_goods.user_id == id).all()
    goods_list = list()
    for i in ug:
        goods_dict = dict()
        goods_dict['id'] = i.goods.id
        goods_dict['gname'] = i.goods.gname
        goods_dict['price'] = i.goods.price
        goods_dict['num'] = i.num

        goods_list.append(goods_dict)
        # print(i.goods)
    message = {
        'code': '200',
        'status': 'success',
        'data': goods_list
    }
    return message
