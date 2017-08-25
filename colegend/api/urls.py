from allauth.account.views import ConfirmEmailView
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework import routers

from colegend.api.schema import schema
from colegend.checkpoints.views import CheckpointViewSet
from colegend.community.views import DuoViewSet, ClanViewSet, TribeViewSet
from colegend.experience.views import ExperienceViewSet
from colegend.journals.views import JournalEntryViewSet
from colegend.office.views import FocusViewSet
from colegend.outcomes.views import OutcomeViewSet
from colegend.roles.views import RoleViewSet
from colegend.studio.views import InterviewEntryViewSet
from colegend.users.views import UserViewSet, GroupViewSet, EmailViewSet
from .views import FacebookLogin, GoogleLogin

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'messages', EmailViewSet, base_name='messages')

router.register(r'outcomes', OutcomeViewSet)
router.register(r'focus', FocusViewSet)

router.register(r'journal', JournalEntryViewSet)
router.register(r'interviews', InterviewEntryViewSet)

router.register(r'duos', DuoViewSet)
router.register(r'clans', ClanViewSet)
router.register(r'tribes', TribeViewSet)

router.register(r'roles', RoleViewSet)
router.register(r'checkpoints', CheckpointViewSet)
router.register(r'experience', ExperienceViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login'),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/', include('rest_auth.urls')),

    # Overwriting https://github.com/Tivix/django-rest-auth/blob/master/rest_auth/registration/urls.py#L12
    # TODO: Implementing a new view that handles this in my client.
    # (or just a notification telling the user that his email has been verified and can continue in the app)
    url(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),
        name='account_confirm_email'),

    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
