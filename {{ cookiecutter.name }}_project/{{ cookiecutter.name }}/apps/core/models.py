{% if cookiecutter.use_mptt == 'y' %}
from mptt.models import MPTTModel, TreeForeignKey
{% endif %}

from django.db import models
{% if cookiecutter.use_mptt == 'y' %}
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls.exceptions import NoReverseMatch

from apps.core import behaviors as bh
from apps.core import common_models as cm
{% endif %}

{% if cookiecutter.use_mptt == 'y' %}
class Page(bh.SEOable, MPTTModel):
    """
    Модель Страница
    """
    title = models.CharField(
        verbose_name='Название',
        max_length=100,
        blank=True
    )
    parent = TreeForeignKey(
        'self',
        verbose_name='Родитель',
        related_name='children',
        blank=True,
        null=True,
        db_index=True
    )
    uri = models.URLField(
        verbose_name='Путь',
        editable=False,
    )
    content_type = models.ForeignKey(
        'contenttypes.ContentType',
        verbose_name='Модель',
        related_name='page_list'
    )
    object_id = models.PositiveIntegerField(
        null=True,
        editable=False
    )
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )

    class MPTTMeta:
        # order_insertion_by = ['tree_id']
        level_attr = 'mptt_level'

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            self.uri = self.get_absolute_url()
        except NoReverseMatch:
            self.uri = reverse('error404')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        if self.object_id:
            try:
                return reverse(
                    '{}_detail'.format(self.content_type.model),
                    kwargs={'pk': self.object_id}
                )
            except NoReverseMatch:
                try:
                    return reverse(
                        '{}_detail'.format(self.content_type.model),
                        kwargs={'slug': self.content_object.slug}
                    )
                except AttributeError:
                    return reverse(
                        '{}_detail'.format(self.content_type.model),
                        kwargs={'slug': self.parent.content_object.slug}
                    )
        else:
            return reverse(
                '{}_list'.format(self.content_type.model)
            )


class Header(MPTTModel):
    """
    Модель страницы в хэдере
    """
    parent = TreeForeignKey(
        'self',
        verbose_name='Родитель',
        related_name='header_child',
        blank=True,
        null=True,
        db_index=True
    )
    page = models.ForeignKey(
        'core.Page',
        verbose_name='Страница',
        related_name='header_menus',
    )

    class MPTTMeta:
        level_attr = 'mptt_level'

    class Meta:
        verbose_name = 'Хэдер'
        verbose_name_plural = 'Хэдер'

    def __str__(self):
        return self.page.title


class Footer(MPTTModel):
    """
    Модель страницы в футере
    """
    parent = TreeForeignKey(
        'self',
        verbose_name='Родитель',
        related_name='footer_child',
        blank=True,
        null=True,
        db_index=True
    )
    page = models.ForeignKey(
        'core.Page',
        verbose_name='Страница',
        related_name='footer_menus',
    )

    class MPTTMeta:
        level_attr = 'mptt_level'

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'

    def __str__(self):
        return self.page.title
{% endif %}
