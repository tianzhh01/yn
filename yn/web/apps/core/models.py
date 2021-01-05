from django.db import models
from common.db_common import BaseModel


class CTI(BaseModel):
    name = models.CharField('表名', max_length=32)
    alias = models.CharField('表别名', max_length=32, null=True, blank=True)
    prefix = models.CharField('表名前缀', max_length=32, null=True, blank=True)

    class Meta:
        verbose_name = "模版-虚拟表"
        db_table = "cti"


class TemplateAttribution(BaseModel):
    name = models.CharField('字段名', max_length=32)
    alias = models.CharField('字段别名', max_length=32, null=True, blank=True)
    type = models.CharField('字段类型', max_length=32)

    readonly = models.BooleanField('只读', default=False)
    required = models.BooleanField('必填', default=False)
    unique = models.BooleanField('唯一', default=False)

    sortable = models.BooleanField('排序', default=True)
    priority = models.IntegerField('优先级', default=100)
    filters = models.CharField('过滤器', max_length=256, null=True, blank=True)
    s_cti = models.ForeignKey('CTI', related_name='+', verbose_name='所属分类', on_delete=models.CASCADE)
    default = models.CharField('默认值', max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = '模板属性'
        db_table = 'template_attribution'


class TemplateRelation(BaseModel):
    name = models.CharField('名称', max_length=32)
    alias = models.CharField('别名', max_length=32)
    s_cti = models.ForeignKey('core.CTI', related_name='+', verbose_name='源分类', on_delete=models.CASCADE)
    t_cti = models.ForeignKey('core.CTI', related_name='+', verbose_name='目标分类', on_delete=models.CASCADE)
    write_back_template = models.ForeignKey('core.CTI', related_name='+', verbose_name='回写模板', on_delete=models.CASCADE)
    write_back_field = models.ForeignKey('core.TemplateAttribution', related_name='+', verbose_name='回写字段',
                                         on_delete=models.CASCADE)
    type = models.CharField('关联类型', max_length=32, blank=True, null=True)

    class Meta:
        verbose_name = '模板关系'
        db_table = 'template_relation'
