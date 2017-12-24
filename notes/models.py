from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class todo(models.Model):

    title = models.TextField()
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def create(self, title, content,user):
        book=todo(title=title,content=content)
        return book

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show',args=[str(self.id)])
