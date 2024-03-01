from rest_framework.serializers import ModelSerializer

from file_manager.models import File


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
