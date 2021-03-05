from django.shortcuts import render

def home(request):
    return render(request, 'forum/home.html')

def about(request):
    return render(request, 'forum/about.html')
