from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from erp.models import Goods, UserProfile
from erp.permissions import IsOwnerOrReadOnly
from erp.serializers import UserSerializer, GroupSerializer, GoodsSerializer, UserProfileSerializer
from erp.utils import WechatLogin


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class GoodsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows goods to be viewed or edited.
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class LoginView(APIView):

    def post(self, request):
        login = WechatLogin(request.data['code'])
        res = login.login()
        return Response(res)
