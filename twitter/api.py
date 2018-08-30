# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from twitter.models import Twitter
from twitter.serializer import TwitterSerializer


class GetTweets(generics.ListAPIView):
    serializer_class = TwitterSerializer
    model = Twitter

    def get_queryset(self):
        queryset = self.model.objects.none()
        input_number = self.request.query_params.get('number')
        if input_number:
            try:
                queryset = Twitter.objects.filter(
                    content__icontains=input_number)
            except:
                queryset = self.model.objects.none()
        return queryset


