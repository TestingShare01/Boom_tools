from rest_framework import serializers
from Tools_User import models
class DevSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Dev
        fields = "__all__"


class TageSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = "__all__"