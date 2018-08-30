# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .api import GetTweets

urlpatterns = [
    url(
        r'^$',
        GetTweets.as_view(),
        name='get_tweets'),
]
