from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, GroupViewSet, FocusViewSet, OutcomeViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'outcomes', OutcomeViewSet)
router.register(r'focus', FocusViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
