from rest_framework.authtoken.models import Token


class AuthorizationMiddleware(object):

    def resolve(self, next, root, info, **args):
        if not info.context.user.is_authenticated:
            token = info.context.META.get('HTTP_AUTHORIZATION')
            if token:
                user = Token.objects.select_related('user').get(key=token).user
                if user:
                    info.context.user = user
        return next(root, info, **args)
