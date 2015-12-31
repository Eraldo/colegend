from django.utils.deconstruct import deconstructible


@deconstructible
class UploadToOwnedDirectory(object):
    # Returns a factory that will generate a user media upload path with an optional sub-directory.
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
        # file will be uploaded to MEDIA_ROOT/users/<id>_<username>/(?:<sub_directory>/)<filename>
        user_attribute = self.user_attribute

        owner = getattr(instance, user_attribute)
        username = owner.username

        sub_directory = self.sub_directory

        template = self.template

        return template.format(username=username, sub_directory=sub_directory, filename=filename)
