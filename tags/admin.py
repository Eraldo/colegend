from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from taggit.admin import TagAdmin as TaggitTagAdmin
from lib.admin import InlineMixin
from tags.models import Tag, TaggedItem
from taggit.models import Tag as TaggitTag

__author__ = 'eraldo'


class TaggedItemInline(InlineMixin, admin.TabularInline):
    model = TaggedItem
    fields = ['content_object', 'content_type', 'object_id']
    extra = 0
    readonly_fields = ('content_object',)

    def content_object(self, instance):
        instance = instance.content_object
        if not instance.id:
            return "(save and then edit)"
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label,  instance._meta.module_name),  args=[instance.id] )
        return u'<a href="{u}">{s}</a>'.format(u=url, s=instance)
    content_object.allow_tags = True


class TagAdmin(TaggitTagAdmin):
    inlines = [
        TaggedItemInline
    ]

admin.site.unregister(TaggitTag)
admin.site.register(Tag, TagAdmin)
