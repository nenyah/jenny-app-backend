from django.contrib import admin
from erp.models import StorageLocation, Validate, Goods


# Register your models here.
@admin.register(StorageLocation)
class StorageLocationAdmin(admin.ModelAdmin):
    fields = ['location', 'parent']


@admin.register(Validate)
class ValidateAdmin(admin.ModelAdmin):
    fields = ['created_by', 'updated_by', 'created_time', 'mfg', 'vali_days', 'exp', 'remain_days']
    readonly_fields = ['created_by', 'updated_by', 'created_time', 'remain_days']


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    fields = ['location', 'validate', 'img', 'name']
    readonly_fields = ['created_by']
