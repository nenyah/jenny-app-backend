import datetime

from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# 通用属性
class CommonInfo(models.Model):
    revision = models.IntegerField('乐观锁', default=0, blank=False)
    created_by = models.CharField(max_length=256, blank=True, verbose_name="创建人", help_text="创建人")
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    is_active = models.BooleanField('是否启用', default=True)

    class Meta:
        abstract = True


# 用户
class UserProfile(CommonInfo):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                parent_link=True,
                                related_name='profile',
                                verbose_name='用户')
    openid = models.CharField('OpenId', max_length=32, blank=False)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        ordering = ('id',)

    def __str__(self):
        return f"{self.user.__str__()}"


# 货物
class Goods(CommonInfo):
    # 基本信息
    img = models.ImageField('图片', upload_to='uploads/', null=True, blank=True)
    name = models.CharField('物品名称', max_length=125)
    location = models.CharField('位置', max_length=32)
    # 有效期
    mfg = models.DateField('生产日期', null=True, blank=True)
    duration = models.IntegerField('有效天数', null=True, blank=True)
    exp = models.DateField('有效日期', null=True, blank=True)

    class Meta:
        verbose_name = '物品'
        verbose_name_plural = verbose_name
        ordering = ('id',)

    def save(self, *args, **kwargs):
        if self.exp is None:
            if self.mfg is None:
                raise Exception("有效日期和生产日期不能同时为空")
            else:
                if self.duration is None:
                    raise Exception("有效天数不能为空")
                self.exp = self.mfg + datetime.timedelta(days=self.duration)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
