from django.db import models
from django.conf import settings
# Create your models here.


class Post(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='relatedcomments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)
    comment_text = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text

# add A Like Field
