from .models import Todo
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TodoSerializer
#Name of modeel follwer by Serializer
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Todo #defined in model class
        # the fields that should be included in the serialized output (converetd to Json)
        fields = ['id', 'subject', 'details']