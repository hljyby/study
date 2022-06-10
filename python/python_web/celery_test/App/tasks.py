# coding:utf-8
import time
from celery_test.celery import app  # 导入celery的实例对象


@app.task
def tsend_email():
    time.sleep(10)
    print('send email ok!')


@app.task
def add(x, y):
    time.sleep(5)
    print(x + y)
    return x + y
