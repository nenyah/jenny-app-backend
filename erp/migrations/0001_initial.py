# Generated by Django 3.2 on 2021-04-15 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.IntegerField(default=0, verbose_name='乐观锁')),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='创建人')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='更新人')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否启用')),
                ('location', models.CharField(max_length=32, verbose_name='位置')),
                ('parent_loc_id', models.IntegerField(null=True, verbose_name='归属位置')),
            ],
            options={
                'verbose_name': 'storage location',
            },
        ),
        migrations.CreateModel(
            name='Validate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.IntegerField(default=0, verbose_name='乐观锁')),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='创建人')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='更新人')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否启用')),
                ('mfg', models.DateField(null=True, verbose_name='生产日期')),
                ('vali_days', models.IntegerField(null=True, verbose_name='有效天数')),
                ('exp', models.DateField(verbose_name='有效日期')),
            ],
            options={
                'verbose_name': 'expire date',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=32, verbose_name='OpenId')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': 'user profile',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.IntegerField(default=0, verbose_name='乐观锁')),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='创建人')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='更新人')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否启用')),
                ('img', models.CharField(max_length=125, verbose_name='图片')),
                ('name', models.CharField(max_length=125, verbose_name='物品名称')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.storagelocation', verbose_name='位置')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.userprofile', verbose_name='用户')),
                ('validate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.validate', verbose_name='有效期')),
            ],
            options={
                'verbose_name': 'goods',
            },
        ),
    ]
