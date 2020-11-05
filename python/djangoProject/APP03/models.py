from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Manager


# class Class(models.Model):
#     cname = models.CharField(max_length=32)
#     cdata = models.DateField()
#
#     # def __str__(self):
#     #     return "%s" % [self.__class__, self.cname]
#
#     class Meta:
#         db_table = 'class'


# class Student(models.Model):
#     sname = models.CharField(max_length=32)
#     cid = models.ForeignKey(to="Class", to_field="id", related_name="student", on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'student'


class StudentDetail(models.Model):
    height = models.PositiveIntegerField()
    email = models.EmailField()
    memo = models.CharField(max_length=128)

    class Meta:
        db_table = 'studentDetail'


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'user'
