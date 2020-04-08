from django.conf import settings
from django.db import models
from django.utils.text import slugify

from rest_framework.reverse import reverse as api_reverse
from account.models import Author
class Article(models.Model):
    author = models.ForeignKey(Author,
                             on_delete=models.CASCADE)
    title = models.name = models.CharField(max_length=500,blank=True, null=True)
    body = models.TextField()
    active = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        ordering = ['timestamp']

    def get_api_url(self, request=None):
        return api_reverse("api-blogs:article-rud", kwargs={'pk': self.pk}, request=request)

