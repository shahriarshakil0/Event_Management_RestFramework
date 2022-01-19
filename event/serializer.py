from rest_framework import serializers
from event.models import *

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id','name','description','location','user']
        depth = 1


# class EventMemberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EventMember
#         fields = "__all__"
#         depth = 1