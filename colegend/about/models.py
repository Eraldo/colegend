from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel, FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from colegend.cms.blocks import BASE_BLOCKS
from colegend.cms.models import UniquePageMixin


class AboutPage(UniquePageMixin, Page):
    template = 'about/about.html'

    content = StreamField(BASE_BLOCKS, blank=True)

    vision_text = models.TextField(blank=True)

    colegend_header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    conscious_header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    connected_header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    continuous_header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    intro_video_id = models.CharField(
        max_length=50,
        blank=True
    )

    apps_teaser_text = RichTextField(
        blank=True,
    )
    community_teaser_text = RichTextField(
        blank=True,
    )
    process_teaser_text = RichTextField(
        blank=True,
    )
    complete_teaser_text = RichTextField(
        blank=True,
    )
    feature_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    reasons_intro = RichTextField(
        blank=True,
    )
    animal_1 = RichTextField(
        blank=True,
    )
    animal_2 = RichTextField(
        blank=True,
    )
    animal_3 = RichTextField(
        blank=True,
    )
    animal_4 = RichTextField(
        blank=True,
    )
    animal_5 = RichTextField(
        blank=True,
    )
    animal_6 = RichTextField(
        blank=True,
    )
    animal_7 = RichTextField(
        blank=True,
    )

    testimonial = RichTextField(
        blank=True,
    )

    pricing_intro = RichTextField(
        blank=True,
    )
    tiger_statement = RichTextField(
        blank=True,
    )

    roles_intro = RichTextField(
        blank=True,
    )

    contact_teaser = RichTextField(
        blank=True,
    )
    feedback_teaser = RichTextField(
        blank=True,
    )

    class Meta:
        verbose_name = _('About')

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
        FieldPanel('vision_text', classname="full"),
        MultiFieldPanel(
            [
                ImageChooserPanel('colegend_header_image'),
                ImageChooserPanel('conscious_header_image'),
                ImageChooserPanel('connected_header_image'),
                ImageChooserPanel('continuous_header_image'),
                FieldPanel('intro_video_id'),
            ],
            heading="Header",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('apps_teaser_text', classname="full"),
                FieldPanel('community_teaser_text', classname="full"),
                FieldPanel('process_teaser_text', classname="full"),
                FieldPanel('complete_teaser_text', classname="full"),
                ImageChooserPanel('feature_image'),
            ],
            heading="Features",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('reasons_intro', classname="full"),
                FieldPanel('animal_1', classname="full"),
                FieldPanel('animal_2', classname="full"),
                FieldPanel('animal_3', classname="full"),
                FieldPanel('animal_4', classname="full"),
                FieldPanel('animal_5', classname="full"),
                FieldPanel('animal_6', classname="full"),
                FieldPanel('animal_7', classname="full"),
            ],
            heading="7 reasons",
            classname="collapsible"
        ),
        FieldPanel('testimonial', classname="full"),
        MultiFieldPanel(
            [
                FieldPanel('pricing_intro', classname="full"),
                FieldPanel('tiger_statement', classname="full"),
            ],
            heading="Pricing",
            classname="collapsible"
        ),
        FieldPanel('roles_intro', classname="full"),
        MultiFieldPanel(
            [
                FieldPanel('contact_teaser', classname="full"),
                FieldPanel('feedback_teaser', classname="full"),
            ],
            heading="Contact",
            classname="collapsible"
        ),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]
