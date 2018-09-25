# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from twitter.models import Twitter
from geopy.geocoders import Nominatim


class TwitterSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField(read_only=True)
    longitude = serializers.SerializerMethodField(read_only=True)

    def get_latitude(self, obj):
        geolocator = Nominatim(user_agent="SSA")
        if not obj.location == "-1":
            if geolocator.geocode(obj.location).latitude:
                return geolocator.geocode(obj.location).latitude
        return 28.6139

    def get_longitude(self, obj):
        geolocator = Nominatim(user_agent="SSA")
        if not obj.location == "-1":
            if geolocator.geocode(obj.location).longitude:
                return geolocator.geocode(obj.location).longitude
        return 77.2090

    class Meta:
        model = Twitter
        fields = '__all__'
