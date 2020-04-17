from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from services.users import views as users

router = routers.SimpleRouter()
router.register('users', users.UserViewSet, base_name='users')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^$', users.UserViewSet.landing)
]
