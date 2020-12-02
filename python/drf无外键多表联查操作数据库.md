# 不使用外键在数据库里的写法



```python
找到了一个解决方案，参考这篇博文重点是django中的ForeignKey与数据库中FOREIGNKEY约束并不一样，ForeignKey是一种逻辑上的关联关系，我们可以指定是否使用数据库中的外键约束。
对于上面的两个Model，可以改写成这样：
classGoods(models.Model):
"""商品表"""
name=models.CharField('名称',max_length=50)
num=models.IntegerField('数量',default=0)
#db_contraints=False表明了使用逻辑上的关联关系，而不需要数据库中的外键约束
shop_id=models.ForeignKey('Shop',on_delete=models.CASCADE,db_contraints=False)
classShop(models.Model):
"""店铺表"""
name=models.CharField('店铺名称',max_length=50)
reputation=models.SmallInteger('店铺信誉',default=1,help_text='范围：1~5')
这样就可以通过外键来实现INNERJOIN查询：queryset=Goods.objects.values('id','num','shop__reputation').order('-num','-shop__reputation')
```

```python
      先用文档中的样例：

      Models定义：

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)
     关系序列化定义：

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('order', 'title', 'duration')

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')
      这个关系序列化有效的前提是必须在model定义中加

related_name='tracks'
     这个设置项，否则tracks在虚拟化结果中会找不到或者报错。
```

# ！！！Django不通过外键查询多对多的数据，数据库表设计不使用外键

# 终于解决了 如何没有通过外键查询多对多的数据，多对一数据

意义： 使用外键，高并发的程序中会产生锁表，影响性能。为了未来的数据库扩展，数据库设计时考虑使用外键，但在实际数据库设计时，将外键的实现放在逻辑层控制。

# 全部的表都是单表

# 解决的办法是通过SerializerMethodField自定义字段来实现。

## model 定义,无外键



```python
# -*- coding:UTF-8 -*-
from django.db import models
#导入django自带的User模型进行扩展
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    """
    用户角色
    """
    role_name = models.CharField(max_length=100,verbose_name="角色名",help_text="角色名")

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name
        #用于指定不同的app使用不同的数据库
        # app_label = "users"
        #使用自定义指定的表明jt_role
        db_table = "jt_role"

    def __str__(self):
        return self.role_name

class Department(models.Model):
    """
    部门
    """
    depat_name = models.CharField(max_length=64, verbose_name="部门名称", help_text="部门名称")

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = verbose_name
        #用于指定不同的app使用不同的数据库
        # app_label = "users"
        #使用自定义指定的表明jt_role
        db_table = "jt_department"

    def __str__(self):
        return self.depat_name

class UserProfile(models.Model):
    """
    在Django的User模型上进行拓展,id字段使用id
    """
    name = models.CharField(max_length=64, verbose_name="姓名")
    depat_id = models.IntegerField(verbose_name="部门id")


    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        #用于指定不同的app使用不同的数据库
        # app_label = "users"
        db_table = "jt_users"

class UserRole(models.Model):
    """
    用户角色关系，为提高性能，不使用manytomany来实现
    """
    user_id = models.IntegerField(verbose_name="用户id")
    role_id = models.IntegerField(verbose_name="角色id")
    is_delete = models.BooleanField(verbose_name="是否逻辑删除", default=False)

    class Meta:
        verbose_name = "用户角色关系"
        verbose_name_plural = verbose_name
        # 使用自定义指定的表明jt_user_role
        db_table = "jt_user_role"
```

## *serializers文件定义*



```python
from rest_framework import serializers
from .models import UserRole,UserProfile,Role,Department

class UserDetailSerializer(serializers.Serializer):
    """
    用户详情序列表类
    """
    name = serializers.CharField()
    depat_name = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ("name", "depat_name","roles")

   #重点中的重点
    def get_roles(self, obj):
        """
        自定义获取多对多数据
        :param obj: 当前user的实例
        :return: 当前用户的全部角色(数组)
        :思路：先通过当前的用户，查询用户角色关系表，获得全部的角色id，再通过角色id获得角色名
        """
        user = obj
        role_ids = UserRole.objects.filter(user_id__exact=user.id).values_list('role_id').all()
        roles = Role.objects.filter(id__in=role_ids).all()
        ret = [ ]
        for item in roles:
            ret.append(item.role_name)
        return ret

    def get_depat_name(self,obj):
        """
        获取部门名称
        :param obj: 当前user的实例
        :return: 当前用户所在部门名称
        """
        user = obj
        depat_name = Department.objects.filter(id = user.depat_id)[0].depat_name
        return depat_name
```

# 实例

```python
测试环境

Win 10

 

Python 3.5.4

 

Django-2.0.13.tar.gz

 

 

需求

不通过外键，使用django orm语法实现多个表之间的关联查询,类似如下sql的查询效果：

SELECT tb_project_version.*, tb_sprint.name, tb_project.name

FROM tb_project_version

JOIN tb_sprint ON tb_sprint.id=tb_project_version.sprint_id

JOIN tb_project ON tb_project.id=tb_project_version.project_id

 

数据表Model设计

 

class Sprint(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='自增id')

    name = models.CharField(max_length=50, verbose_name='迭代名称')

    ...略   

 

    class Meta:

        db_table = 'tb_sprint'

        verbose_name = '产品迭代表'

        verbose_name_plural = verbose_name

 

class Project(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='自增id')

    name = models.CharField(max_length=50, verbose_name='项目名称')

    ...略

 

    class Meta:

        db_table = 'tb_project'

        verbose_name = '项目表'

        verbose_name_plural = verbose_name

 

 

class ProjectVersion(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='自增id')

    name = models.CharField(max_length=50, verbose_name='版本名称')

    project_id = models.IntegerField(verbose_name='关联的项目ID')

    sprint_id = models.IntegerField(verbose_name='关联的迭代ID')

    ...略

   

    class Meta:

        db_table = 'tb_project_version'

        verbose_name = '项目版本表'

        verbose_name_plural = verbose_name

 

实现方法1-通过extra api函数实现

 

如下，带背景色部分的内容为核心

 

serializers.py

#!/usr/bin/env python

# -*- coding:utf-8 -*-

 

from rest_framework import serializers

from backend.models import ProjectVersion

 

# ProjectVersion model 序列化器

class ProjectVersionSerializer(serializers.ModelSerializer):

    project = serializers.CharField(required=True)

    sprint = serializers.CharField(required=True)

 

    class Meta:

        model = ProjectVersion

        fields = '__all__'

        read_only_fields = ['project', 'sprint']

 

说明：如上，如果使用了django rest framework序列化，则需要为其序列化器添加model中不存在的字段，否则序列化后还是看不到对应的目标字段

 

project_version_views.py

#!/usr/bin/env python

# -*- coding:utf-8 -*-

 

__author__ = '授客'

 

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

 

from backend.models import ProjectVersion

from backend.serializers import ProjectVersionSerializer

 

 

 

class ProjectVersionListAPIView(APIView):

    '''

    项目视图-版本管理

    '''

    # 查询列表数据

    def get(self, request, format=None):

        result = {}

        try:

            params =  request.GET

            page_size = int(params.get('pageSize'))

            page_no = int(params.get('pageNo'))

            name = params.get('name')

            project_id = params.get('projectId')

            sort = params.get('sort')

            if sort:

                sort_list = sort.split(',')

            else:

                sort_list = ['-id']

 

            startIndex = (page_no - 1) * page_size

            endIndex = startIndex + page_size

            filters = {'is_delete':0}

            if name:

                filters['name__startswith'] = name

            if project_id:

                filters['project_id'] = project_id

            projectVersions = ProjectVersion.objects.filter(**filters).extra(

                select={'project': 'SELECT tb_project.name FROM tb_project WHERE tb_project.id = tb_project_version.project_id',

                        'sprint':'SELECT tb_sprint.name FROM tb_sprint WHERE tb_sprint.id = tb_project_version.sprint_id'},

            )

rows = projectVersions.order_by(*sort_list)[startIndex:endIndex]

            rows = ProjectVersionSerializer(rows, many=True).data

            total = projectVersions.count()

 

            result['msg'] =  '获取成功'

            result['success'] =  True

            result['data'] = {}

            result['data']['rows'] = rows

            result['data']['total'] = total

            return Response(result, status.HTTP_200_OK)

        except Exception as e:

            result['msg'] =  '%s' % e

            result['success'] =  False

            return Response(result, status.HTTP_500_INTERNAL_SERVER_ERROR)

 

说明：

projectVersions.order_by(*sort_list)[startIndex:endIndex]

 

等价于

 

SELECT (SELECT tb_project.name FROM tb_project WHERE tb_project.id = tb_project_version.project_id) AS `project`,

(SELECT tb_sprint.name FROM tb_sprint WHERE tb_sprint.id = tb_project_version.sprint_id) AS `sprint`,

`tb_project_version`.`id`,

`tb_project_version`.`name`,

`tb_project_version`.`project_id`,

`tb_project_version`.`sprint_id`,

...略

FROM `tb_project_version`

WHERE `tb_project_version`.`is_delete` = 0

ORDER BY `tb_project`.`id` DESC LIMIT 10 # 假设startIndex=0, endIndex=10

 

projectVersions.count()

等价于

SELECT COUNT(*) AS `__count` FROM `tb_project_version`

WHERE `tb_project_version`.`is_delete` = 0

 

 

 

上述查询代码的另一种实现

projectVersions =  Project.objects.filter(**filters).extra(

select={'project:'tb_project.name',

        'sprint':' tb_sprint.name',

tables=['tb_project', 'tb_sprint'],

where=['tb_project.id=tb_project_version.project_id', 'tb_sprint.id = tb_project_version.sprint_id']

)

rows = projectVersions.order_by(*sort_list)[startIndex:endIndex]

rows = ProjectVersionSerializer(rows, many=True).data

total = projectVersions.count()

 

 

projectVersions.order_by(*sort_list)[startIndex:endIndex]

 

等价于

 

SELECT (tb_project.name) AS `project`,

(tb_sprint.name) AS `sprint`,

`tb_project_version`.`id`,

`tb_project_version`.`name`,

`tb_project_version`.`project_id`,

`tb_project_version`.`sprint_id`,

...略

FROM `tb_project_version`

WHERE `tb_project_version`.`is_delete` = 0 AND (tb_project.id=tb_project_version.project_id) AND (tb_sprint.id = tb_project_version.sprint_id)

ORDER BY `tb_project`.`id` DESC LIMIT 10 # 假设startIndex=0, endIndex=10

 

 

projectVersions.count()

等价于

SELECT COUNT(*) AS `__count` FROM `tb_project_version` , `tb_project` , `tb_sprint` WHERE `tb_project_version`.`is_delete` = 0 AND (tb_project.id=tb_project_version.project_id) AND (tb_sprint.id = tb_project_version.sprint_id)

 

 

实现方法2-通过django rest framework实现

serializers.py

#!/usr/bin/env python

# -*- coding:utf-8 -*-

 

from rest_framework import serializers

from backend.models import ProjectVersion

from backend.models import Sprint

from backend.models import Project

 

 

# ProjectVersion model 序列化器

class ProjectVersionSerializer(serializers.ModelSerializer):

    project = serializers.SerializerMethodField()

    sprint = serializers.SerializerMethodField()

 

    def get_sprint(self, obj):

        """

        :param obj: 当前ProjectVersion的实例

        """

        current_project_version = obj

        sprint = Sprint.objects.filter(id=current_project_version.sprint_id).first()

        if sprint:

            return sprint.name

        else:

            return '--'

 

    def get_project(self, obj):

        """

        :param obj: 当前ProjectVersion的实例

        """

        current_project_version = obj

        project = Project.objects.filter(id=current_project_version.project_id).first()

        if project:

            return project.name

        else:

            return '--'

 

    class Meta:

        model = ProjectVersion

        fields = '__all__'

        read_only_fields = ['project', 'sprint']

 

project_version_views.py

#!/usr/bin/env python

# -*- coding:utf-8 -*-

 

__author__ = '授客'

 

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

 

from backend.models import ProjectVersion

from backend.serializers import ProjectVersionSerializer

 

 

 

class ProjectVersionListAPIView(APIView):

    '''

    项目视图-版本管理

    '''

    # 查询列表数据

    def get(self, request, format=None):

        result = {}

        try:

            params =  request.GET

            page_size = int(params.get('pageSize'))

            page_no = int(params.get('pageNo'))

            name = params.get('name')

            project_id = params.get('projectId')

            sort = params.get('sort')

            if sort:

                sort_list = sort.split(',')

            else:

                sort_list = ['-id']

 

            startIndex = (page_no - 1) * page_size

            endIndex = startIndex + page_size

            filters = {'is_delete':0}

            if name:

                filters['name__startswith'] = name

            if project_id:

                filters['project_id'] = project_id

            rows = ProjectVersion.objects.filter(**filters).order_by(*sort_list)[startIndex:endIndex]

            rows = ProjectVersionSerializer(rows, many=True).data

            total = ProjectVersion.objects.filter(**filters).count()

 

            result['msg'] =  '获取成功'

            result['success'] =  True

            result['data'] = {}

            result['data']['rows'] = rows

            result['data']['total'] = total

            return Response(result, status.HTTP_200_OK)

        except Exception as e:

            result['msg'] =  '%s' % e

            result['success'] =  False

            return Response(result, status.HTTP_500_INTERNAL_SERVER_ERROR)

 

方法3-通过raw函数执行原生sql

以下是项目中的一个实例，和本文上述内容没有任何关联，关键部分背景已着色，笔者偷懒，不做过多解释了，简单说下下面这段代码对用途：

 

主要是实现类似以下查询，获取指定分页对数据以及满足条件的记录记录总数。

 

SELECT tb_project.*, project_name_associated, project_id_associated, platform FROM tb_project

LEFT JOIN tb_project_associated ON tb_project.id=tb_project_associated.project_id

ORDER BY id DESC

LIMIT 0,10

 

 

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from backend.models import Project

from backend.serializers import ProjectSerializer

 

import logging

 

 

logger = logging.getLogger('mylogger')

 

class ProjectListAPIView(APIView):

    '''

    项目视图-项目管理-项目列表

    '''

 

    # 查询列表数据

    def get(self, request, format=None):

        result = {}

        try:

            params =  request.GET

            page_size = int(params.get('pageSize'))

            page_no = int(params.get('pageNo'))

            name = params.get('name')

            project_status = params.get('status')

            sort = params.get('sort')

 

            order_by = 'id desc'

            if sort:

                order_by = sort

          

            startIndex = (page_no - 1) * page_size

 

            where = 'WHERE tb_project.is_delete=0 '

            filters = {'is_delete':0}

            if name:

                filters['name__startswith'] = name

                where += 'AND locate("%s", name) ' % name

 

            if project_status:

                where += "AND status='%s'" % project_status

 

            sql = 'SELECT tb_project.id, COUNT(1) AS count FROM tb_project LEFT JOIN tb_project_associated ON tb_project.id=tb_project_associated.project_id '

            query_rows = Project.objects.raw(sql)

            total = query_rows[0].__dict__.get('count') if query_rows else 0

 

            sql =  'SELECT tb_project.*,project_name_associated, project_id_associated, platform FROM tb_project LEFT JOIN tb_project_associated ON tb_project.id=tb_project_associated.project_id ' \

                    '%s ORDER BY %s ' \

                    'LIMIT %s,%s ' % (where,order_by, startIndex, page_size)

            query_rows = Project.objects.raw(sql)

            rows = []

            for item in query_rows:

                item.__dict__.pop('_state')

                item.__dict__['create_time'] = item.__dict__['create_time'].strftime('%Y-%m-%d %H:%M:%S')

                item.__dict__['update_time'] = item.__dict__['update_time'].strftime('%Y-%m-%d %H:%M:%S')

                item.__dict__['begin_time'] = item.__dict__['begin_time'].strftime('%Y-%m-%d')

                item.__dict__['end_time'] = item.__dict__['end_time'].strftime('%Y-%m-%d')

                rows.append(item.__dict__)

        

            result['msg'] =  '获取成功'

            result['success'] =  True

            result['data'] = {}

            result['data']['rows'] = rows

            result['data']['total'] = total

            return Response(result, status.HTTP_200_OK)

        except Exception as e:

            result['msg'] =  '%s' % e

            result['success'] =  False

            return Response(result, status.HTTP_500_INTERNAL_SERVER_ERROR)
```

