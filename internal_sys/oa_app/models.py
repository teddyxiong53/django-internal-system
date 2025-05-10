from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title = models.CharField('标题', max_length=200)
    content = models.TextField('内容')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField('发布日期', auto_now_add=True)

    def __str__(self):
        return self.title
