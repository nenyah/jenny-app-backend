# Generated by Django 3.2 on 2021-04-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_auto_20210416_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validate',
            name='exp',
            field=models.DateField(null=True, verbose_name='有效日期'),
        ),
    ]
