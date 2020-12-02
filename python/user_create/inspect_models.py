# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group'


class Rule(models.Model):
    rule_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    rule_level = models.IntegerField()
    parents_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule'


class RuleGroup(models.Model):
    rule_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_group'


class User(models.Model):
    user_name = models.CharField(max_length=255)
    status = models.IntegerField()
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255, blank=True, null=True)
    register_ip = models.CharField(max_length=255, blank=True, null=True)
    login_ip = models.CharField(max_length=255, blank=True, null=True)
    login_num = models.IntegerField(blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    is_check = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    admin_check = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserGroup(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group'
