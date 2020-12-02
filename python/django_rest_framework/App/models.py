from django.db import models


# Create your models here.
class Column(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='栏目', help_text='姓名')
    link_url = models.URLField(verbose_name='链接')
    index = models.IntegerField(verbose_name='位置')
    email = models.EmailField()

    class Meta:  # 模型元选项
        db_table = 'tb_column'  # 在数据库中的表名，否则Django自动生成为app名字_类名
        ordering = ['index']
        verbose_name = '栏目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
