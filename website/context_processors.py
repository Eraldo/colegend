from django.conf import settings

__author__ = 'eraldo'


def offline(request):
    """
    A django context processor that adds information about the desired connection type.
    Example usage: In a template load the local scripts instead of CDN version.

    :param request:
    :return: Returns a context dictionary
    """
    return {'offline': settings.OFFLINE}
