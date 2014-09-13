from allauth.account.adapter import DefaultAccountAdapter
from users.models import Contact, Profile

__author__ = 'eraldo'


class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_username, user_field

        data = form.cleaned_data

        username = data.get('username')
        user_username(user, username)

        email = data.get('email')
        user_email(user, email)

        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)

        # Create and fill in contact.
        contact_fields = ["first_name", "last_name", "gender", "birthday",
                          "phone_number",
                          "street", "postal_code", "city", "country"]
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
            contact.user = user
            contact.save()
            profile.user = user
            profile.save()
        return user
