from django.contrib.auth.models import User, Group
from rest_framework import serializers
from erp.models import UserProfile, Goods, StorageLocation, Validate


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    password = serializers.CharField(
        style={'input_type': 'password'}, label=True, write_only=True
    )

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'openid', 'created_by']

    # 获取当前登录的用户
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name', 'created_by']

    # 获取当前登录的用户
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = ['location', 'validate', 'img', 'name', 'created_by', 'updated_by']

    # 获取当前登录的用户
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class StorageLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StorageLocation
        fields = ['location', 'parent', 'created_by', 'updated_by']

    # 获取当前登录的用户
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class ValidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Validate
        fields = ['mfg', 'vali_days', 'exp', 'remain_days', 'created_by', 'updated_by']

    # 获取当前登录的用户
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
