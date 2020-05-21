from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AudioFileViewSet, UserViewSet


# urlpatterns=[
#     path('<int:pk>/', AudioFileDetail.as_view()),
#     path('', AudioFileList.as_view()),
# ]

router=DefaultRouter()
router.register('users', UserViewSet, basename="users")
router.register('waevs', AudioFileViewSet, basename="waevs")

urlpatterns=router.urls