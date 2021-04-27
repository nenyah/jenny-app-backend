from django.contrib import admin
from erp.models import Goods, UserProfile


# Register your models here.


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    exclude = ('revision', 'created_by')
    fields = []
    list_display = ('name', 'location', 'exp')
    search_fields = list_display
    list_filter = list_display


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fields = []
