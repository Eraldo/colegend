from django import forms


class OwnedModelForm(forms.ModelForm):
    def clean_owner(self):
        owner = self.cleaned_data.get('owner')
        if not owner == self.owner:
            message = 'You need to be the owner.'
            self.add_error(None, message)
        return owner
