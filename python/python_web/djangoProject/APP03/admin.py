from django.contrib import admin

# Register your models here.
from APP03.models import StudentDetail, User


class StudentDetailAdmin(admin.ModelAdmin):
    list_display = ['email', 'memo']  # 展示什么字段
    search_fields = ['pk']
    # 分页
    list_per_page = 5
    # 过滤字段
    list_filter = ['memo']


admin.site.register(StudentDetail, StudentDetailAdmin)
admin.site.register(User)
