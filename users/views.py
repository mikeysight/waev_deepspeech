from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import UserRegisterForm

# Create your views here.
@api_view(['GET'])
def current_user(request):
    user = request.user
    print(user)
    return Response({
        'id': user.id,
        'username': user.username
    })

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'waev/register.html', {'form': form})