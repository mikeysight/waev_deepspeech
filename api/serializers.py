from rest_framework import serializers

from waev.models import AudioFile

class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = (
            'id',
            'filename',
            'audio', 
            'transcript', 
            'user',
        )