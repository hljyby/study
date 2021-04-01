from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update = models.DateTimeField(blank=True, null=True, auto_now=True)
    is_del = models.IntegerField(default=1)

    class Meta:
        db_table = 'group'
        verbose_name = '组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.group_name


class Rule(models.Model):
    rule_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(default=1)
    rule_level = models.IntegerField()
    parents_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update = models.DateTimeField(blank=True, null=True, auto_now=True)
    is_del = models.IntegerField(default=1)
    group_ = models.ForeignKey('Group', related_name='group_rule')

    class Meta:
        db_table = 'rule'
        verbose_name = '权限'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.rule_name


class RuleGroup(models.Model):
    rule_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update = models.DateTimeField(blank=True, null=True, auto_now=True)
    is_del = models.IntegerField(default=1)

    class Meta:
        db_table = 'rule_group'
        verbose_name = '权限组'
        verbose_name_plural = verbose_name


class User(models.Model):
    username = models.CharField(max_length=255, unique=True, name='username')
    status = models.IntegerField(default=1)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255, blank=True, null=True)
    register_ip = models.CharField(max_length=255, blank=True, null=True)
    login_ip = models.CharField(max_length=255, blank=True, null=True)
    login_num = models.IntegerField(blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    is_check = models.IntegerField(blank=True, null=True, default=1)
    unit = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    admin_check = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update = models.DateTimeField(blank=True, null=True, auto_now=True)
    is_del = models.IntegerField(default=1)
    code = models.CharField(max_length=255, blank=True, null=True, )

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserGroup(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update = models.DateTimeField(blank=True, null=True, auto_now=True)
    is_del = models.IntegerField(default=1)

    class Meta:
        db_table = 'user_group'
        verbose_name = '用户——组中间表'
        verbose_name_plural = verbose_name
