{% if cookiecutter.use_mptt == 'y' -%}
from mptt.admin import DraggableMPTTAdmin
{%- endif %}
{% if cookiecutter.use_jet_admin == 'y' -%}
from jet.admin import CompactInline
{%- endif %}

from django.contrib import admin
from django.contrib.auth.models import User, Group

{% if cookiecutter.use_mptt == 'y' -%}
from apps.core import models
{%- endif %}

{% if cookiecutter.use_mptt == 'y' -%}
{% if cookiecutter.use_jet_admin == 'y' -%}
class TextBlockInline(CompactInline):
{%- else %}
class TextBlockInline(admin.StackedInline):
{%- endif %}
    model = models.TextBlock
    extra = 0


class PageAdmin(DraggableMPTTAdmin):
    inlines = [TextBlockInline]
    mptt_level_indent = 50
    readonly_fields = ['uri']
    fieldsets = (
        ('Основные', {
            'fields': ('title', 'parent', 'content_type', 'uri')
        }),
        ('SEO', {
            'classes': ('collapse',),
            'fields': ('seo_title', 'seo_keywords', 'seo_description'),
        })
    )


class HeaderAdmin(DraggableMPTTAdmin):
    form = HeaderForm
    mptt_level_indent = 50


class FooterAdmin(DraggableMPTTAdmin):
    form = FooterForm
    mptt_level_indent = 50
{% endif -%}


admin.site.unregister(User)
admin.site.unregister(Group)
{% if cookiecutter.use_mptt == 'y' -%}
admin.site.register(models.Page, PageAdmin)
admin.site.register(models.Header, HeaderAdmin)
admin.site.register(models.Footer, FooterAdmin)
{%- endif %}
