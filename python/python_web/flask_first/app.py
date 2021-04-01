from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from apps import create_app
from ext import db

# 必须添加 添加后才可以映射到数据库
from apps.user import models
from apps.article import models

app = create_app(__name__)

manager = Manager(app=app)

# 命令工具
migrate = Migrate(app=app, db=db)

# 生成 命令和 @manager.command 一样
manager.add_command('db', MigrateCommand)


# python app.py db init
# python app.py db migrate
# python app.py db upgrade
# 执行上述三个命令在数据库里生成对应的表

# Flask-Migrate    2.5.3
# Flask-Script     2.0.6
# Flask-SQLAlchemy 2.4.4

@manager.command
def init():
    print('Hello World!')


@app.route('/')
def home():
    return 'home'


if __name__ == '__main__':
    manager.run()
