from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save, post_delete

from rest_framework.reverse import reverse as api_reverse


class UserRegistration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=120, null=True, blank=True)
    token_access = models.TextField(null=True, blank=True)
    token_refresh = models.TextField(null=True, blank=True)
    verification_code = models.CharField(max_length=6, null=True, blank=True)
    terms = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return str(self.user)


class Account(models.Model):
    slug = models.SlugField(unique=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=120, null=True, blank=True)
    phone_number = models.CharField(max_length=120, null=True, blank=True)
    telephone = models.CharField(max_length=120, null=True, blank=True)
    token_access = models.TextField(null=True, blank=True)
    token_refresh = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=False)
    term = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.user)

    @property
    def owner(self):
        return self.user

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.user))
        super(Account, self).save(*args, **kwargs)

    class Meta:
        ordering = ['timestamp']

    def get_api_url(self, request=None):
        return api_reverse("api-accounts:account-rud", kwargs={'pk': self.pk}, request=request)


class WalletPin(models.Model):
    account_holder = models.ForeignKey(Account, on_delete=models.CASCADE)
    pin = models.CharField(max_length=500, null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return str(self.account_holder)
