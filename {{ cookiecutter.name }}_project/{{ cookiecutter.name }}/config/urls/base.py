from django.conf.urls import url
from django.contrib import admin

from core.views import IndexView

urlpatterns = [
    url(
        regex=r'^$',
        view=IndexView.as_view(),
        name='index'
    ),
    {% if cookiecutter.use_jet_admin == 'y' %}
    url(
        regex=r'^jet/',
        view=include('jet.urls', 'jet')
    ),
    url(
        regex=r'^jet/dashboard/',
        view=include('jet.dashboard.urls', 'jet-dashboard')
    ),
    {% endif %}
    url(
        regex=r'^admin/',
        view=admin.site.urls
    ),
]
