# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from rest_framework import generics
from twitter.models import Twitter
from twitter.serializer import TwitterSerializer


class GetTweets(generics.ListAPIView):
    serializer_class = TwitterSerializer
    model = Twitter

    def get_queryset(self):
        cleaned_number = None
        queryset = self.model.objects.none()
        input_number = self.request.query_params.get('number')
        if input_number:
            cleaned_number = re.sub('[ -/A-z]', '', input_number)
        if cleaned_number and len(cleaned_number) > 6:
            try:
                queryset = Twitter.objects.filter(
                    numbers__icontains=cleaned_number)
            except:
                queryset = self.model.objects.none()
        return queryset


