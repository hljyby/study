# coding:utf-8
import time
from djangoProject.celery import app  # 导入celery的实例对象
from celery import shared_task
from celery.signals import task_success

@app.task
def tsend_email():
    time.sleep(10)
    print('send email ok!')


@app.task
def add(x, y):
    time.sleep(5)
    return x + y
