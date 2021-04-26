from django.contrib.auth.models import User, Group
from rest_framework import serializers
from erp.models import UserProfile, Goods, Position, Validate


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


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

    # 获取当前登录的用户
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class ValidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Validate
        fields = '__all__'

    # 获取当前登录的用户
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'position', 'validate', 'img', 'name', 'created_by', 'url']

    position = PositionSerializer()

    validate = ValidateSerializer(required=False)
    # 获取当前登录的用户
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def create(self, validated_data):
        print(validated_data)
        location_data = validated_data.pop("position")
        validate_data = validated_data.pop("validate")
        position = Position.objects.create(**location_data)
        # 如果没有 validate 就不用创建
        tmp_validate = dict(validate_data)
        if tmp_validate['mfg'] is not None or tmp_validate['exp'] is not None:
            validate = Validate.objects.create(**validate_data)
            validated_data['validate'] = validate
        validated_data['position'] = position
        goods = Goods.objects.create(**validated_data)
        return goods

    def update(self, instance, validated_data):
        return instance
