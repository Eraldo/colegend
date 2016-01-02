from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, RedirectView

from guides.models import GuideRelation
from .forms import GuideManageForm


class GuideIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'guides/introduction.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            # update connected path
            user = request.user
            user.connected.guide_introduction = True
            user.connected.save()
            # redirect to profile
            return redirect('guides:guide')
        return self.get(request, *args, **kwargs)


class GuideListView(LoginRequiredMixin, ListView):
    template_name = 'guides/list.html'
    model = GuideRelation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        relations = self.get_queryset()
        context['searching_relations'] = relations.searching()
        context['active_relations'] = relations.active()
        context['passive_relations'] = relations.passive()
        return context


class GuideesView(LoginRequiredMixin, ListView):
    template_name = 'guides/guidees.html'
    model = GuideRelation

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        return queryset.filter(guide=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        relations = self.get_queryset()
        context['active_relations'] = relations.active()
        context['passive_relations'] = relations.passive()
        return context


class GuideDetailView(LoginRequiredMixin, DetailView):
    template_name = 'guides/detail.html'
    model = GuideRelation

    def get(self, request, *args, **kwargs):
        user = request.user
        relation = self.get_object()
        if user == relation.owner:
            return redirect('guides:guide')
        elif user == relation.guide:
            return redirect('guides:manage', relation.owner)
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        return GuideRelation.objects.get(owner__username=owner)


class GuideView(LoginRequiredMixin, DetailView):
    template_name = 'guides/guide.html'
    model = GuideRelation

    def get(self, request, *args, **kwargs):
        connected = request.user.connected
        if not connected.guide_introduction:
            return redirect('guides:introduction')
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        user = self.request.user
        return user.guiderelation


class GuideManageView(LoginRequiredMixin, UpdateView):
    template_name = 'guides/manage.html'
    form_class = GuideManageForm

    def get_object(self, queryset=None):
        user = self.request.user
        owner = self.kwargs.get('owner')
        guidee_relations = user.guidee_relations.all()
        try:
            relation = guidee_relations.get(owner__username=owner)
            return relation
        except GuideRelation.DoesNotExist:
            raise Http404

    def get_success_url(self):
        relation = self.get_object()
        return reverse('guides:detail', kwargs={'owner': relation.owner})


class GuideActionView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        owner = self.kwargs.get('owner')
        # Update relation
        relation = GuideRelation.objects.get(owner__username=owner)
        relation.guide = user
        relation.save()
        return relation.get_absolute_url()
