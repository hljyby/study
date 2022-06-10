"""
Django settings for celery_test project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v#j6_+o(vsmv9v0_2p(dy%@p80&lwd&$a&j3gg_48__gsn$5h%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App.apps.AppConfig',
    'djcelery'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'celery_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'celery_test.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'celery',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'Zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

######django-celery配置######
# import djcelery
# from celery.schedules import timedelta, crontab
#
# djcelery.setup_loader()  # 开始加载当前所有安装app中的task
#
# # 使用redis代理来分发任务
# BROKER_URL = 'redis://192.168.0.200:6379/8'
# CELERY_IMPORTS = ('App.tasks')  # 导入任务，可以执行的异步任务
# CELERY_TIMEZONE = 'Asia/Shanghai'  # 中国时区
#
# # 任务存入到数据库中
# # CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
#
# CELERYD_CONCURRENCY = 2  # celery worker并发数
# CELERYD_MAX_TASKS_PER_CHILD = 5  # 每个worker最大执行任务数 执行5个就销毁
# CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 后端存储任务超过一天则自动清理

# # 定时器策略
# CELERYBEAT_SCHEDULE = {
#     # 定时任务一：每隔30s运行一次
#     u'邮件发送': {
#         "task": "App.tasks.tsend_email",  # 有必要注意该位置的post指tasks.py所在文件夹tsend_email为异步函数之一
#         # "schedule": crontab(minute='*/2'),
#         "schedule": timedelta(seconds=5),
#         "args": (),
#     },
#     u'性能计算': {
#         "task": "App.tasks.add",
#         "schedule": crontab(minute='*/2'),
#         "args": (1, 4),
#     },
# }

#####django-celery end########

# import time
#
# cur_path = os.path.dirname(os.path.realpath(__file__))  # log_path是存放日志的路径
# log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# if not os.path.exists(log_path): os.mkdir(log_path)  # 如果不存在这个logs文件夹，就自动创建一个
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         # 日志格式
#         'standard': {
#             'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
#                       '[%(levelname)s]- %(message)s'},
#         'simple': {  # 简单格式
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     # 过滤
#     'filters': {
#         # 要求debug false 才记录
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     # 定义具体处理日志的方式
#     'handlers': {
#         'mail_admins': {  # 上线后出错邮件报错
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'filters': ['require_debug_false']
#         },
#         # 默认记录所有日志
#         'default': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(log_path, 'all-{}.log'.format(time.strftime('%Y-%m-%d'))),
#             'maxBytes': 1024 * 1024 * 5,  # 文件大小
#             'backupCount': 5,  # 备份数
#             'formatter': 'standard',  # 输出格式
#             'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
#         },
#         # 输出错误日志
#         'error': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(log_path, 'error-{}.log'.format(time.strftime('%Y-%m-%d'))),
#             'maxBytes': 1024 * 1024 * 5,  # 文件大小
#             'backupCount': 5,  # 备份数
#             'formatter': 'standard',  # 输出格式
#             'encoding': 'utf-8',  # 设置默认编码
#         },
#         'debug': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(log_path, 'debug-{}.log'.format(time.strftime('%Y-%m-%d'))),
#             'maxBytes': 1024 * 1024 * 5,  # 文件大小
#             'backupCount': 5,  # 备份数
#             'formatter': 'standard',  # 输出格式
#             'encoding': 'utf-8',  # 设置默认编码
#         },
#         # 控制台输出
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#         # 输出info日志
#         'info': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(log_path, 'info-{}.log'.format(time.strftime('%Y-%m-%d'))),
#             'maxBytes': 1024 * 1024 * 5,
#             'backupCount': 5,
#             'formatter': 'standard',
#             'encoding': 'utf-8',  # 设置默认编码
#         },
#     },
#     # 配置用哪几种 handlers 来处理日志
#     'loggers': {
#         # 类型 为 django 处理所有类型的日志， 默认调用
#         'django': {
#             'handlers': ['default', 'console'],
#             'level': 'INFO',
#             'propagate': False  # 继承父类的信息
#         },
#         'django.request': {  # 用户请求发生错误
#             'handlers': ['debug', 'mail_admins'],
#             'level': 'ERROR',
#             'propagate': True  # 继承父类的信息
#         },
#         # log 调用时需要当作参数传入
#         'log': {
#             'handlers': ['error', 'info', 'console', 'default'],
#             'level': 'INFO',
#             'propagate': True
#         },
#     }
# }

ADMINS = (('yby', '2694286031@qq.com'),)
# 发送邮件设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 固定写法
EMAIL_HOST = 'smtp.163.com'  # SMTP地址
EMAIL_PORT = 25  # SMTP端口
EMAIL_HOST_USER = '18249241924@163.com'  # 发送邮件的邮箱
EMAIL_HOST_PASSWORD = 'LGAGMGHTETRLUCRQ'  # 授权码
EMAIL_SUBJECT_PREFIX = '[杨xx测试] '  # 为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)默认false
DEFAULT_FROM_EMAIL = '贪婪玩月客服中心<18249241924@163.com>'  # 收件人看到的发件人<此处要和发邮件的邮箱相同>

# 配置邮件
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = EMAIL_HOST_USER
