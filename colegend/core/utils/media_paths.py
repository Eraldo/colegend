from django.contrib.auth import get_user_model
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadToOwnedDirectory:
    """
    Returns a factory that will generate a user media upload path with an optional sub-directory.
    Files will be uploaded to MEDIA_ROOT/users/<username>/(?:<sub_directory>/)<filename>
    """
    template = "users/{username}/{sub_directory}{filename}"
    user_attribute = 'owner'
    sub_directory = ''

    def __init__(self, sub_directory=None, user_attribute=None):
        if sub_directory:
            if not sub_directory.endswith('/'):
                sub_directory += '/'
            self.sub_directory = sub_directory
        if user_attribute:
            self.user_attribute = user_attribute

    def __call__(self, instance, filename):
        if isinstance(instance, get_user_model()):
            owner = instance
        else:
            owner = getattr(instance, self.user_attribute)

        return self.template.format(
            username=owner.username,
            sub_directory=self.sub_directory,
            filename=filename
        )


@deconstructible
class UploadToAppModelDirectory:
    """
    Returns a factory that will generate a generic media upload path with an optional sub-directory.
    Files will be uploaded to MEDIA_ROOT/<app>/<model>/(?:<sub_directory>/)<filename>
    """
    template = '{app}/{model}/{sub_directory}{filename}'
    sub_directory = ''

    def __init__(self, sub_directory=None):
        if sub_directory:
            if not sub_directory.endswith('/'):
                sub_directory += '/'
            self.sub_directory = sub_directory

    def __call__(self, instance, filename):
        return self.template.format(
            app=instance._meta.app_label,
            model=instance._meta.model_name,
            sub_directory=self.sub_directory,
            filename=filename
        )
