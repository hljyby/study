from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from apps import create_app
from ext import db

import apps.user.model

app = create_app(__name__)

manager = Manager(app=app)

# 命令工具
migrate = Migrate(app=app, db=db)

# 生成 命令和 @manager.command 一样
manager.add_command('db', MigrateCommand)


@manager.command
def init():
    print('Hello World!')


@app.route('/')
def home():
    return 'home'


if __name__ == '__main__':
    manager.run()
