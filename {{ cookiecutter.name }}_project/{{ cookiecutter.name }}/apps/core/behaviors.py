from datetime import date

from django.db import models
from django.core.validators import RegexValidator
from django.utils.html import format_html
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail, ResizeToFill

from apps.core.utils import upload


class Titleable(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=400
    )

    class Meta:
        abstract = True


class Subtitleable(models.Model):
    subtitle = models.CharField(
        verbose_name='Подзаголовок',
        max_length=200
    )

    class Meta:
        abstract = True


class Textable(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        blank=True
    )

    class Meta:
        abstract = True


class Descriptionable(models.Model):
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )

    class Meta:
        abstract = True


class ShortDescriptionable(models.Model):
    short_description = models.TextField(
        verbose_name='Краткое описание',
        blank=True
    )

    class Meta:
        abstract = True


class Imageable(models.Model):
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to=upload,
        options={'optimize': True}
    )

    class Meta:
        abstract = True


class DescImageable(models.Model):
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to=upload,
        options={'optimize': True},
        blank=True
    )

    image_description = models.TextField(
        verbose_name='Описание изображения',
        blank=True
    )

    class Meta:
        abstract = True


class Plane2dable(models.Model):
    plane_2d = ProcessedImageField(
        verbose_name='Плоская планировка',
        upload_to=upload,
        options={'optimize': True},
        blank=True
    )

    class Meta:
        abstract = True


class Plane3dable(models.Model):
    plane_3d = ProcessedImageField(
        verbose_name='Объемная планировка',
        upload_to=upload,
        options={'optimize': True},
        blank=True
    )

    class Meta:
        abstract = True


class CharNumberable(models.Model):
    number = models.CharField(
        verbose_name='Номер',
        max_length=20,
    )

    class Meta:
        abstract = True


class IntNumberable(models.Model):
    number = models.PositiveSmallIntegerField(
        verbose_name='Номер'
    )

    class Meta:
        abstract = True


class Emailable(models.Model):
    email = models.EmailField(
        verbose_name='Электронная почта'
    )

    class Meta:
        abstract = True


class Phoneable(models.Model):
    phone_regex = RegexValidator(
        regex=r'(8|\+7)(\s|\-)?(\d{3}|\(\d{3}\))(\s|\-)?\d{3}(\s|\-)?\d{2}(\s|\-)?\d{2}',
        message='Формат ввода телефонного номера +79012346767'
    )
    phone = models.CharField(
        validators=[phone_regex],
        verbose_name='Контактный телефон',
        max_length=20,
        blank=True
    )

    class Meta:
        abstract = True


class SVGable(models.Model):
    svg = models.TextField(
        verbose_name='SVG',
        blank=True
    )

    class Meta:
        abstract = True


class Dateable(models.Model):
    date = models.DateField(
        verbose_name='Дата'
    )

    class Meta:
        abstract = True


class Fileable(models.Model):
    file = models.FileField(
        verbose_name='Файл',
        upload_to=upload
    )

    class Meta:
        abstract = True


class Styleable(models.Model):
    background_color = models.CharField(
        verbose_name='Цвет фона',
        max_length=7,
        blank=True
    )
    is_white = models.BooleanField(
        verbose_name='Белый цвет шрифта?',
        default=False,
    )

    class Meta:
        abstract = True


class SEOable(models.Model):
    seo_title = models.CharField(
        verbose_name='Заголовок',
        max_length=68,
        blank=True
    )
    seo_keywords = models.CharField(
        verbose_name='Ключевые слова',
        max_length=150,
        blank=True
    )
    seo_description = models.TextField(
        verbose_name='Мета описание',
        blank=True
    )

    class Meta:
        abstract = True


class Nameable(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=50
    )

    class Meta:
        abstract = True


class Positionable(models.Model):
    latitude = models.DecimalField(
        verbose_name='Широта',
        max_digits=9,
        decimal_places=6
    )
    longitude = models.DecimalField(
        verbose_name='Долгота',
        max_digits=9,
        decimal_places=6
    )

    class Meta:
        abstract = True


class Publishable(models.Model):
    published = models.BooleanField(
        verbose_name='Опубликовано',
        default=False
    )

    class Meta:
        abstract = True


class Previewable(models.Model):
    px_300 = ImageSpecField(
        source='image',
        processors=[Thumbnail(width=300)]
    )
    px_260x140 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(260, 140)]
    )
    px_60x60 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(60, 60)]
    )
    px_50x50 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(50, 50)]
    )
    px_40x40 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(40, 40)]
    )

    def preview(self):
        return format_html('<img src="{}"/>', self.px_300.url)

    preview.short_description = 'Превью'

    class Meta:
        abstract = True


class Orderable(models.Model):
    order = models.PositiveIntegerField(
        verbose_name='Порядок',
        default=0,
    )

    class Meta:
        abstract = True


class URLable(models.Model):
    url = models.URLField(
        verbose_name='URL',
        max_length=200
    )

    class Meta:
        abstract = True
