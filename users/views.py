from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def current_user(request):
    user = request.user
    print(user)
    return Response({
        'id': user.id,
        'username': user.username
    })