from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'user'  # 指定表名


'''
python manage.py makemigrations # 生成数据库迁移文件
python manage.py migrate #生成数据库表
python manage.py # 获取帮助
'''
