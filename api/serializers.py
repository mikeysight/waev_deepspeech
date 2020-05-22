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
    audiofile_set=serializers.SerializerMethodField()
    class Meta:
        fields=(
            'id',
            'username',
            'audiofile_set'
        )
        model = User
    def get_audiofile_set(self, instance):
        waevs=instance.audiofile_set.all().order_by('-date_modified')
        return AudioFileSerializer(waevs, many=True).data