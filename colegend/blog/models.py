from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase, Tag
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet

from colegend.cms.blocks import BASE_BLOCKS
from colegend.cms.models import UniquePageMixin


class BlogPage(UniquePageMixin, Page):
    template = 'blog/index.html'
    @property
    def articles(self):
        articles = BlogArticlePage.objects.descendant_of(self).live()
        articles = articles.order_by(
            '-date'
        ).select_related('owner').prefetch_related(
            'tagged_items__tag',
        )
        return articles

    class Meta:
        verbose_name = _('Blog')

    subpage_types = ['blog.BlogArticlePage']


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogArticlePage', related_name='tagged_items')


@register_snippet
class BlogTag(Tag):
    class Meta:
        proxy = True


class BlogArticlePage(Page):
    template = 'blog/article.html'

    content = StreamField(BASE_BLOCKS, blank=True)

    date = models.DateField(
        _("Display date"), default=timezone.now().date(),
        help_text=_("This date may be displayed on the blog article. It is not "
                    "used to schedule posts to go live at a later date.")
    )
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Image')
    )
    color = models.CharField(
        max_length=80,
        verbose_name=_('Color'),
        blank=True,
    )

    class Meta:
        verbose_name = _('Blog article')
        verbose_name_plural = _('Blog articles')

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
        ImageChooserPanel('image'),
        FieldPanel('color'),
        FieldPanel('tags'),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('date'),
    ]

    search_fields = Page.search_fields + (
        index.SearchField('content'),
    )

    parent_page_types = ['blog.BlogPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['image'] = self.image.get_rendition('max-1200x1200').url if self.image else ''
        return context

    def get_blog(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(BlogPage).last()
