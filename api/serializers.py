from rest_framework import serializers
from django.contrib.auth.models import User
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
class UserSerializer(serializers.ModelSerializer):
    audiofile_set=AudioFileSerializer(read_only=True, many=True)
    class Meta:
        fields=(
            'id',
            'username',
            'audiofile_set'
        )
        model = User