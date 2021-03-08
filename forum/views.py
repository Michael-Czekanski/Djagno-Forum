from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Topic
from .forms import TopicCreateForm, PostCreateForm

def home(request):
    topics_with_latest_posts = []
    for topic in Topic.objects.order_by('-creation_date'):
        latest_post = topic.post_set.order_by('-date_posted').first()
        topics_with_latest_posts.append((topic, latest_post))

    content = {
        'topics_with_latest_posts': topics_with_latest_posts
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

    if request.user.is_authenticated:
        if request.method == 'POST':
            post_form = PostCreateForm(request.POST, user=request.user, topic=topic)
            if post_form.is_valid():
                post_form.save()
                return redirect('forum-topic', topic_id=topic_id)
        else:
            post_form = PostCreateForm(user=request.user, topic=topic)
    else:
        post_form = None

    content = {
        'topic': topic,
        'posts': posts,
        'post_form': post_form
    }

    return render(request, 'forum/topic.html', content)

@login_required
def topic_create(request):
    if request.method == 'POST':
        topic_form = TopicCreateForm(request.POST, user=request.user)
        post_form = PostCreateForm(request.POST, user=request.user, topic=topic_form.instance)
        if topic_form.is_valid() and post_form.is_valid():
            topic_form.save()
            post_form.save()
            return redirect('forum-topic', topic_id=topic_form.instance.id)
    else:
        topic_form = TopicCreateForm(user=request.user)
        post_form = PostCreateForm(user=request.user, topic=topic_form.instance)

    content = {
        'topic_form': topic_form,
        'post_form': post_form
    }
    return render(request, 'forum/topic_create.html', content)
