from rest_framework import generics

from waev.models import AudioFile
from .permissions import IsAuthorOrReadOnly
from .serializers import AudioFileSerializer

class AudioFileList(generics.ListCreateAPIView):
    queryset = AudioFile.objects.all()
    serializer_class = AudioFileSerializer

class AudioFileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = AudioFile.objects.all()
    serializer_class = AudioFileSerializer

