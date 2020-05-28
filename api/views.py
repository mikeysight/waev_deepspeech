from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User
from django.http import HttpResponse
from waev.models import AudioFile
from .permissions import IsAuthorOrReadOnly
from .serializers import AudioFileSerializer, UserSerializer

# class AudioFileList(generics.ListCreateAPIView):
#     queryset = AudioFile.objects.all()
#     serializer_class = AudioFileSerializer

# class AudioFileDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = AudioFile.objects.all()
#     serializer_class = AudioFileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthorOrReadOnly]

class AudioFileViewSet(viewsets.ModelViewSet):
    queryset=AudioFile.objects.all()
    serializer_class = AudioFileSerializer
    # permission_classes = [IsAuthorOrReadOnly]






