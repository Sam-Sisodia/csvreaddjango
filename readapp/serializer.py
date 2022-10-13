
from rest_framework import serializers

from .models import *


# class countryserilizer(serializers.ModelSerializer):
#     class Meta:
#         model = Country
#         fields = "__all__"


class fileuploadserilizer(serializers.Serializer):
    file= serializers.FileField()


