from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import Tag, TagBase, ItemBase
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from colegend.cms.blocks import BASE_BLOCKS


class BlogPage(Page):
    template = 'blog/index.html'

    @property
    def posts(self):
        posts = BlogPostPage.objects.descendant_of(self).live()
        posts = posts.order_by(
            '-date'
        ).select_related('owner').prefetch_related(
            'tagged_items__tag',
        )
        return posts

    @property
    def tags(self):
        return BlogTag.objects.all()

    class Meta:
        verbose_name = _('Blog')

    subpage_types = ['blog.BlogPostPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        posts = self.posts
        # owners = posts.values_list('owner', flat=True)
        tag = request.GET.get('tag')
        if tag:
            context['tag'] = tag
            posts = posts.filter(tags__slug=tag)
        owner = request.GET.get('owner')
        if owner:
            context['owner'] = owner
            posts = posts.filter(owner__username=owner)
        context['posts'] = posts
        context['tags'] = self.tags
        return context


@register_snippet
class BlogTag(TagBase):
    class Meta:
        verbose_name = _("Blog tag")
        verbose_name_plural = _("Blog tags")


class TaggedBlogPostPage(ItemBase):
    content_object = ParentalKey('BlogPostPage', related_name='tagged_items')
    tag = models.ForeignKey(
        to=BlogTag,
        related_name="%(app_label)s_%(class)s_items",
        on_delete=models.CASCADE
    )


class BlogPostPage(Page):
    template = 'blog/post.html'

    lead = models.TextField(
        verbose_name=_('Lead text'),
        blank=True,
    )
    content = StreamField(
        BASE_BLOCKS,
        blank=True,
    )
    date = models.DateField(
        verbose_name=_('Display date'), default=timezone.now,
        help_text=_("This date may be displayed on the blog post. It is not "
                    "used to schedule posts to go live at a later date.")
    )
    tags = ClusterTaggableManager(
        through=TaggedBlogPostPage,
        blank=True
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Image')
    )
    PINK = '#f72e74'
    ORANGE = '#FFAB40'
    YELLOW = '#eede39'
    GREEN = '#a8e141'
    CYAN = '#6bdaed'
    BLUE = '#3197d6'
    PURPLE = '#ad86fc'
    DARK = '#455A64'
    COLOR_CHOICES = (
        (PINK, _('pink')),
        (ORANGE, _('orange')),
        (YELLOW, _('yellow')),
        (GREEN, _('green')),
        (CYAN, _('cyan')),
        (BLUE, _('blue')),
        (PURPLE, _('purple')),
        (DARK, _('dark')),
    )
    color = models.CharField(
        max_length=80,
        verbose_name=_('Color'),
        blank=True,
        choices=COLOR_CHOICES,
    )

    class Meta:
        verbose_name = _('Blog post')
        verbose_name_plural = _('Blog posts')

    content_panels = Page.content_panels + [
        FieldPanel('lead'),
        StreamFieldPanel('content'),
        ImageChooserPanel('image'),
        FieldPanel('color'),
        FieldPanel('tags'),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('date'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('lead'),
        index.SearchField('content'),
    ]

    parent_page_types = ['blog.BlogPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['image'] = self.image.get_rendition('max-1200x1200').url if self.image else ''
        context['color'] = self.color or self.DARK
        return context

    def get_blog(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(BlogPage).last()
