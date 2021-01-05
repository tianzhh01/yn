from django.db import models


class BaseModel(models.Model):
    create_user = models.CharField('创建用户', max_length=64, blank=True, null=True)
    write_user = models.CharField('更新用户', max_length=64, blank=True, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    write_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True
