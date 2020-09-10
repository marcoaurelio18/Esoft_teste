from django.contrib.auth import logout
from django.shortcuts import render, redirect



def home(request):
    return render(request, 'home/home.html')


# Função para logout e encaminhar para a home
def my_logout(request):
    logout(request)
    return redirect('home')