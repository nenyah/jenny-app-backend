from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# 用户
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile', verbose_name='用户')
    openid = models.CharField('OpenId', max_length=32, blank=False)

    class Meta:
        verbose_name = 'user profile'

    def __str__(self):
        return f"{self.user.__str__()}"


# 通用属性
class CommonInfo(models.Model):
    revision = models.IntegerField('乐观锁', default=0, blank=False)
    created_by = models.CharField('创建人', max_length=32, null=True, blank=True)
    updated_by = models.CharField('更新人', max_length=32, null=True, blank=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    is_active = models.BooleanField('是否启用', default=False)

    class Meta:
        abstract = True


# 储藏位置
class StorageLocation(CommonInfo):
    location = models.CharField('位置', max_length=32)
    parent_loc_id = models.IntegerField('归属位置', null=True)

    class Meta:
        verbose_name = 'storage location'

    def __str__(self):
        return f"{self.location}"


# 效期
class Validate(CommonInfo):
    mfg = models.DateField('生产日期', null=True)
    vali_days = models.IntegerField('有效天数', null=True)
    exp = models.DateField('有效日期')

    class Meta:
        verbose_name = 'expire date'

    def __str__(self):
        return f"有效期：{self.exp}"


# 货物
class Goods(CommonInfo):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE, verbose_name='位置')
    validate = models.ForeignKey(Validate, on_delete=models.CASCADE, verbose_name='有效期')
    img = models.CharField('图片', max_length=125)
    name = models.CharField('物品名称', max_length=125)

    class Meta:
        verbose_name = 'goods'

    def __str__(self):
        return f"物品: {self.name}"
