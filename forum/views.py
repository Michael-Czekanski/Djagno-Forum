from django.shortcuts import render
from django.http import Http404
from .models import Topic

def home(request):

    content = {
        'topics': Topic.objects.order_by('-creation_date')
    }
    return render(request, 'forum/home.html', content)

def about(request):
    return render(request, 'forum/about.html')

def topic(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        raise Http404("Topic does not exist")

    posts = topic.post_set.all()

    content = {
        'topic': topic,
        'posts': posts
    }

    return render(request, 'forum/topic.html', content)
