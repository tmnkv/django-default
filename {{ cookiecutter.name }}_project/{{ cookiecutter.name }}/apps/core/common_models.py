from django.db import models

from apps.core import behaviors as bh


class Common(models.Model):
    created = models.DateTimeField(
        verbose_name='Время и дата создания',
        auto_now_add=True,
        editable=False
    )
    modified = models.DateTimeField(
        verbose_name='Время и дата изменения',
        auto_now=True,
        editable=False
    )

    class Meta:
        abstract = True


class Ordered(bh.Orderable, Common):

    class Meta:
        abstract = True
