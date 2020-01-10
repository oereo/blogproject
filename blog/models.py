from django.db import models
from datetime import datetime

#Create your models here.

# class Blog(models.Model):
#     title = models.CharField(max_length = 200)
#     pub_date = models.DateTimeField('date published')
#     body = models.TextField()

#     def __str__(self):
#         return self.title

#     def summary(self):
#         return self.body[:100]

# class Comment(models.Model):
#     blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='comments')
#     author = models.CharField(max_length=200)
#     text = models.TextField()

#     def __str__(self):
#         return self.text

class Blog(models.Model):
    user_id = models.IntegerField()
    owner = models.CharField(max_length=20, default="???")
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    body = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def increaseViews(self):
        self.views +=1
        self.save()

class Comment(models.Model):
    blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.text