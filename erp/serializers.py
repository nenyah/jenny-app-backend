from django.contrib.auth.models import User, Group
from rest_framework import serializers
from erp.models import UserProfile, Goods


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    password = serializers.CharField(
        style={'input_type': 'password'}, label="密码", write_only=True
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
        fields = ['id', 'user', 'openid', 'created_by']

    user = UserSerializer
    # 获取当前登录的用户
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name', 'created_by']

    # 获取当前登录的用户
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'img', 'name', 'location', 'mfg', 'duration', 'exp', 'created_by', 'url']

    # 获取当前登录的用户
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
