from ext import db
from datetime import datetime


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gname = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    User_goods = db.relationship('User_goods', backref='goods')

    # user = db.relationship('User', backref='goods', secondary='user_goods') # 多对多表关系 用secondary=中间表名

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # https://www.cnblogs.com/aibabel/p/11571196.html
    # Integer
    # String
    # Datetime
    def __str__(self):
        return self.gname


class User_goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'), nullable=False)
    num = db.Column(db.Integer, default=1)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
