from rest_framework import viewsets

from colegend.experience.models import add_experience
from colegend.scopes.models import DAY, get_scope_by_name
from .serializers import InterviewEntrySerializer
from .models import InterviewEntry


class InterviewEntryViewSet(viewsets.ModelViewSet):
    queryset = InterviewEntry.objects.all()
    serializer_class = InterviewEntrySerializer
    filter_fields = ['scope', 'start']

    def get_queryset(self):
        user = self.request.user
        return user.interview_entries.all()

    def filter_queryset(self, queryset):
        scope = self.request.query_params.get('scope')
        start = self.request.query_params.get('start')
        if scope and start and scope != DAY:
            # Update start to match correct scope start date.
            start = get_scope_by_name(scope)(start).start
            params = self.request.query_params
            params._mutable = True
            params['start'] = str(start)
            params._mutable = False
        return super().filter_queryset(queryset)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # Add experience.
        user = serializer.instance.owner
        add_experience(user, 'studio')
