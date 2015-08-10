from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.utils import valid_email_or_none
from users.models import Contact, Profile
from allauth.account.utils import user_email, user_username, user_field

__author__ = 'eraldo'


class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        data = form.cleaned_data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        username = data.get('username')
        user_email(user, email)
        user_username(user, username)
        user_field(user, 'first_name', first_name or '')
        user_field(user, 'last_name', last_name or '')
        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)

        # Create and fill in contact.
        contact_fields = ["phone_number",
                          "street", "postal_code", "city", "country",
                          "gender", "birthday"]
        contact_data = {key: value for key, value in data.items() if key in contact_fields}
        contact = Contact(**contact_data)

        # Create and fill in profile.
        profile_fields = [
            'origin', "referrer", 'experience', 'motivation', 'change', 'drive', 'expectations', 'other',
            'stop', 'discretion', 'responsibility', 'appreciation', 'terms',
        ]
        profile_data = {key: value for key, value in data.items() if key in profile_fields}
        profile = Profile(**profile_data)

        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
            contact.owner = user
            contact.save()
            profile.owner = user
            profile.save()
        return user


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self,
                      request,
                      sociallogin,
                      data):
        """
        Hook that can be used to further populate the user instance.

        For convenience, we populate several common fields.

        Note that the user instance being populated represents a
        suggested User instance that represents the social user that is
        in the process of being logged in.

        The User instance need not be completely valid and conflict
        free. For example, verifying whether or not the username
        already exists, is not a responsibility.
        """
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        name = data.get('name')
        user = sociallogin.user
        user_username(user, username or first_name or last_name or '')
        user_email(user, valid_email_or_none(email) or '')
        name_parts = (name or '').partition(' ')
        user_field(user, 'first_name', first_name or name_parts[0])
        user_field(user, 'last_name', last_name or name_parts[2])
        return user

