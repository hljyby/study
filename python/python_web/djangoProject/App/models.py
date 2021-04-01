# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Manager


class MyManager(Manager):
    def get_queryset(self):
        data = super().get_queryset()
        data = data.filter(sex__isnull=False)
        return data


class ArticleContent(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    isdelete = models.IntegerField()
    tid = models.IntegerField()
    update_date = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article_content'


class ArticleTab(models.Model):
    tab = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'article_tab'

    # user_manager = Manager()  # 管理器 如果不自定义就会出现objects 为默认管理器
    # sex_manager = MyManager()  # 自定义管理器，现在使用这个sex_manager 会把数据进行过滤

