# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from twitter.models import Twitter


class TwitterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Twitter
        fields = '__all__'
