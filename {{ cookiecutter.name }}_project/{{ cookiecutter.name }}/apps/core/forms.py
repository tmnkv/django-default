{% if cookiecutter.use_mptt == 'y' -%}
from mptt.forms import TreeNodeChoiceField

{%- endif %}
from django.forms import ModelForm, Select
{% if cookiecutter.use_mptt == 'y' -%}
from apps.core.models import Page, Header, Footer


class HeaderForm(ModelForm):
    parent = TreeNodeChoiceField(
        label='Родитель',
        queryset=Header.objects.all(),
        widget=Select(attrs={'class': 'selector'}),
        required=False
    )
    page = TreeNodeChoiceField(
        label='Страница',
        queryset=Page.objects.all(),
        widget=Select(attrs={'class': 'selector'}),
        required=True
    )

    class Meta:
        model = Header
        fields = '__all__'


class FooterForm(HeaderForm):
    parent = TreeNodeChoiceField(
        label='Родитель',
        queryset=Footer.objects.all(),
        widget=Select(attrs={'class': 'selector'}),
        required=False
    )

    class Meta:
        model = Footer
        fields = '__all__'
{%- endif %}
