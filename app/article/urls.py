from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ArticleDetailView, ArticleCreateView, ArticleList

urlpatterns = [
    url(r'^create/(?P<pk>\d+)/$', ArticleCreateView, name='article-create'),
    url(r'^$', ArticleList.as_view(), name='article-list'),
    url(r'^(?P<pk>\d+)/$', ArticleDetailView, name='article-rud'),
]