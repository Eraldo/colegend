from django.forms import ModelForm

from .models import AdventureReview


class AdventureReviewForm(ModelForm):
    class Meta:
        model = AdventureReview
        fields = [
            'owner', 'adventure',
            'rating', 'image_url', 'content'
        ]
