from rest_framework import serializers

from .models import Focus


class FocusSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.name')

    class Meta:
        model = Focus
        fields = [
            'url', 'id', 'owner',
            'scope', 'start',
            'outcome_1', 'outcome_2', 'outcome_3', 'outcome_4',
            'created', 'modified',
        ]

    def validate(self, attrs):
        scope = attrs.get('scope')
        fields = ['outcome_1', 'outcome_2', 'outcome_3', 'outcome_4']
        for field in fields:
            outcome = attrs.get(field)
            if outcome and outcome.scope != scope:
                # raise serializers.ValidationError('Scope mismatch.')
                error = {field: ['Scope mismatch.']}
                raise serializers.ValidationError(error)
        return super().validate(attrs)
