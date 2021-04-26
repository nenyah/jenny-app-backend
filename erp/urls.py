from django.urls import include, path
from rest_framework import routers
from erp import views

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'usersprofile', views.UserProfileViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'goods', views.GoodsViewSet)
router.register(r'locations', views.StorageLocationViewSet)
router.register(r'validates', views.ValidateViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('v1/', include(router.urls)),
]
