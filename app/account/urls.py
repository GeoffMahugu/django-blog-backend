from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import AuthorSignupView, AuthorList, AuthorDetailView

urlpatterns = [
    url(r'^$', AuthorList.as_view(), name='author-list'),
    url(r'^(?P<pk>\d+)/$', AuthorDetailView, name='author-rud'),
    url(r'^signup/$', AuthorSignupView, name='author-signup'),
]