from django.contrib.auth.models import User, Group
from rest_framework import serializers
from erp.models import UserProfile, Goods, StorageLocation, Validate


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = ['location', 'validate', 'img', 'name']


class StorageLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StorageLocation
        fields = ['location', 'parent']


class ValidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Validate
        fields = ['mfg', 'vali_days', 'exp']
