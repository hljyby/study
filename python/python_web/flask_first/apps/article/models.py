from ext import db
from datetime import datetime


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    like = db.Column(db.Integer, default=0)
    content = db.Column(db.Text, nullable=False)
    save = db.Column(db.Integer, default=0)
    click = db.Column(db.Integer, default=0)
    create_date = db.Column(db.DateTime, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # https://www.cnblogs.com/aibabel/p/11571196.html
    # Integer
    # String
    # Datetime
    def __str__(self):
        return self.title
