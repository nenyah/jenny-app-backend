import datetime

from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# 通用属性
class CommonInfo(models.Model):
    revision = models.IntegerField('乐观锁', default=0, blank=False)
    created_by = models.ForeignKey(User,
                                   related_name="%(app_label)s_%(class)s_related",
                                   verbose_name='创建人',
                                   related_query_name="%(app_label)s_%(class)ss",
                                   on_delete=models.CASCADE)
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
        verbose_name = 'user profile'

    def __str__(self):
        return f"{self.user.__str__()}"


# 储藏位置
class StorageLocation(CommonInfo):
    location = models.CharField('位置', max_length=32)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               verbose_name='归属位置',
                               null=True,
                               blank=True)

    class Meta:
        verbose_name = 'storage location'
        ordering = ('id',)

    def __str__(self):
        return f"{self.location}"


# 效期
class Validate(CommonInfo):
    mfg = models.DateField('生产日期', null=True)
    vali_days = models.IntegerField('有效天数', null=True)
    exp = models.DateField('有效日期', null=True)

    def remain_days(self):
        """
        Use the exp to calculate the remain days.
        :return: remain days int
        """
        today = datetime.date.today()
        exp = self.exp
        return (exp - today).days if (exp - today).days > 0 else 0

    remain_days.admin_order_field = 'exp'
    remain_days.short_description = '到期天数'

    class Meta:
        verbose_name = 'expire date'
        ordering = ['exp']

    def save(self, *args, **kwargs):
        """
        Use the mfg and validays generate exp.
        """
        if self.exp is None:
            if self.mfg is None:
                raise Exception("生产日期和有效日期不能都为空")
            else:
                if self.vali_days is None:
                    raise Exception("有效天数不能为空")
                else:
                    delta = datetime.timedelta(days=self.vali_days)
                    self.exp = self.mfg + delta
        super().save(*args, **kwargs)

    def __str__(self):
        return f"有效期：{self.exp}"


# 货物
class Goods(CommonInfo):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE, verbose_name='位置')
    validate = models.OneToOneField(Validate, on_delete=models.CASCADE, verbose_name='有效期', null=True, blank=True)
    img = models.ImageField('图片')
    name = models.CharField('物品名称', max_length=125)

    class Meta:
        verbose_name = 'goods'
        verbose_name_plural = verbose_name
        ordering = ('id',)

    def __str__(self):
        return f"物品:[{self.id}. {self.name}]"
