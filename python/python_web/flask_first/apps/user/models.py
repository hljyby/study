from ext import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    article = db.relationship('Article', backref='user')
    User_goods = db.relationship('User_goods', backref='user')

    # 这个字段在模板层面
    # https://www.cnblogs.com/aibabel/p/11571196.html
    def __str__(self):
        return self.username

