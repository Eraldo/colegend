from rest_framework.authtoken.models import Token


class AuthorizationMiddleware:
    """
    Add the authenticated user to the context.
    (Unless the user is not active.)
    """
    def resolve(self, next, root, info, **args):
        if not info.context.user.is_authenticated:
            token = info.context.META.get('HTTP_AUTHORIZATION')
            if token:
                user = Token.objects.select_related('user').get(key=token).user
                if user and user.is_active:
                    info.context.user = user
        return next(root, info, **args)
