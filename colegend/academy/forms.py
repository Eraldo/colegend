from django.forms import ModelForm

from .models import BookReview


class BookReviewForm(ModelForm):
    class Meta:
        model = BookReview
        fields = [
            'owner', 'book',
            'rating', 'area_1', 'area_2', 'area_3', 'area_4', 'area_5', 'area_6', 'area_7', 'content'
        ]
