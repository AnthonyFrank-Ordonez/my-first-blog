from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    """Post Object"""
    # properties/object propterties
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # actions/methods
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comments=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    """Comments Model"""

     # properties/object propterties
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comments = models.BooleanField(default=False)

    # actions/methods
    def approve(self):
        self.approved_comments = True
        self.save()
    
    def __str__(self):
        return self.text