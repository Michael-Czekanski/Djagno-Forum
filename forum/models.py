from django.db import models
from django.utils import timezone
from users.models import User

class Topic(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_latest_post(self):
        """
        Returns latest post from this topic.
        """

        return self.post_set.order_by('-date_posted').first()

    def get_posts_count(self):
        """
        Returns topic's posts count.
        """

        return self.post_set.count()

class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, models.CASCADE)
    post_number = models.IntegerField(editable=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['topic', 'post_number'],
            name='unique_topic_post_num')
        ]


    def save(self, *args, **kwargs):
        self.post_number = self.topic.get_posts_count() + 1
        super().save(*args, **kwargs)


    def __str__(self):
        result = f'{self.topic.name}, {self.author.username}: {self.content[:10]}'
        if len(self.content) > 10:
            result += ' ...'
        return result


    def content_short(self):
        if len(self.content) < 10:
            return self.content
        else:
            return self.content[:10] + ' ...'
