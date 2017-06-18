from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, GroupViewSet, FocusViewSet, OutcomeViewSet, FacebookLogin, GoogleLogin

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'outcomes', OutcomeViewSet)
router.register(r'focus', FocusViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login'),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
]
