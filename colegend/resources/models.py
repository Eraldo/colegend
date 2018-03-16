from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TagBase, ItemBase
from wagtail.admin.edit_handlers import StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from colegend.cms.blocks import BASE_BLOCKS


class ResourcesPage(Page):
    template = 'resources/index.html'

    content = StreamField(BASE_BLOCKS, blank=True)

    @property
    def tags(self):
        return ResourceTag.objects.all()

    @property
    def resources(self):
        return ResourcePage.objects.descendant_of(self).live()

    class Meta:
        verbose_name = _('Resources Page')

    subpage_types = ['resources.ResourcePage']

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        resources = self.resources
        # owners = posts.values_list('owner', flat=True)
        tag = request.GET.get('tag')
        if tag:
            context['tag'] = tag
            resources = resources.filter(tags__slug=tag)
        context['resources'] = resources
        context['tags'] = self.tags
        return context


@register_snippet
class ResourceTag(TagBase):
    class Meta:
        verbose_name = _('Resource tag')
        verbose_name_plural = _('Rescource tags')


class TaggedResourcePage(ItemBase):
    content_object = ParentalKey('ResourcePage', related_name='tagged_items')
    tag = models.ForeignKey(
        to=ResourceTag,
        related_name="%(app_label)s_%(class)s_items",
        on_delete=models.CASCADE
    )


class ResourcePage(Page):
    template = 'resources/resource.html'

    lead = models.TextField(
        verbose_name=_('Lead text'),
        blank=True,
    )

    content = StreamField(BASE_BLOCKS, blank=True)

    area_1 = models.IntegerField(
        verbose_name=_('Health'),
        validators=[MinValueValidator(-100), MaxValueValidator(100)],
    )

    area_2 = models.IntegerField(
        verbose_name=_('Joy'),
        validators=[MinValueValidator(-100), MaxValueValidator(100)],
    )

    area_3 = models.IntegerField(
        verbose_name=_('Power'),
        validators=[MinValueValidator(-100), MaxValueValidator(100)],
    )

    area_4 = models.IntegerField(
        verbose_name=_('Connection'),
        validators=[MinValueValidator(-100), MaxValueValidator(100)],
    )

    area_5 = models.IntegerField(
        verbose_name=_('Expression'),
        validators=[MinValueValidator(-100), MaxValueValidator(100)],
    )

    area_6 = models.IntegerField(
        verbose_name=_('Mind'),
        validators=[MinValueValidator(-100), MaxValueValidator(100)],
    )

    area_7 = models.IntegerField(
        verbose_name=_('Spirit'),
        validators=[MinValueValidator(-100), MaxValueValidator(100)],
    )

    tags = ClusterTaggableManager(
        through=TaggedResourcePage,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('lead'),
        MultiFieldPanel(
            [
                FieldPanel('area_1'),
                FieldPanel('area_2'),
                FieldPanel('area_3'),
                FieldPanel('area_4'),
                FieldPanel('area_5'),
                FieldPanel('area_6'),
                FieldPanel('area_7'),
            ],
            heading="Life area impact",
            classname="collapsible",
        ),
        FieldPanel('tags'),
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + [
        index.FilterField('area_1'),
        index.FilterField('area_2'),
        index.FilterField('area_3'),
        index.FilterField('area_4'),
        index.FilterField('area_5'),
        index.FilterField('area_6'),
        index.FilterField('area_7'),
        index.SearchField('lead'),
        index.SearchField('content'),
    ]

    parent_page_types = ['resources.ResourcesPage']

    class Meta:
        verbose_name = _('Resource Page')

