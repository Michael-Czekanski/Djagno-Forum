from django import forms
from .models import Topic, Post

class TopicCreateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']

    def __init__(self, *args, **kwargs):
        created_by = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.instance.created_by = created_by


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

    def __init__(self, *args, **kwargs):
        author = kwargs.pop('user')
        topic = kwargs.pop('topic')
        super().__init__(*args, **kwargs)
        self.instance.author = author
        self.instance.topic = topic
