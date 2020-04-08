from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ArticleRudView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ArticleRudView.as_view(), name='article-rud'),
]