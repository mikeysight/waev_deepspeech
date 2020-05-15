from django.urls import path
from .views import AudioFileList, AudioFileDetail

urlpatterns=[
    path('<int:pk>/', AudioFileDetail.as_view()),
    path('', AudioFileList.as_view())
]