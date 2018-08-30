# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django_mysql.models import ListTextField


class Twitter(models.Model):
    tweet_id = models.CharField(null=True, blank=True, max_length=200)
    keyword = models.CharField(null=True, blank=True, max_length=200)
    username = models.CharField(null=True, blank=True, max_length=200)
    user_id = models.CharField(null=True, blank=True, max_length=200)
    content = models.TextField(null=True, blank=True)
    timestamp = models.CharField(null=True, blank=True, max_length=200)
    location = models.CharField(null=True, blank=True, max_length=200)
    hashtag = ListTextField(
        base_field=models.CharField(null=True, blank=True, max_length=200),
        size=100
    )
    retweet = models.CharField(null=True, blank=True, max_length=200)
    favourite = models.CharField(null=True, blank=True, max_length=200)
    source = models.CharField(null=True, blank=True, max_length=200)
    date_added = models.CharField(null=True, blank=True, max_length=200)
    in_reply_to = models.CharField(null=True, blank=True, max_length=200)
    region = models.CharField(null=True, blank=True, max_length=200)
    numbers = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _('Tweet data')

    def __unicode__(self):
        return str(self.tweet_id)

    def __str__(self):
        return str(self.tweet_id)
