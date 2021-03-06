from django.shortcuts import render
from .models import Topic

def home(request):

    content = {
        'topics': Topic.objects.all()
    }
    return render(request, 'forum/home.html', content)

def about(request):
    return render(request, 'forum/about.html')
