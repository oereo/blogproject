from django.db import models
from datetime import datetime
from django.conf import settings

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


def user_path(instance, filename): # instance는 Photo 클래스의 객체, filename은 업로드할 파일의 파일이름
    from random import choice   # string으로 나온 결과에서 하나의 문자열만 뽑아냄
    import string               # 무작위 문자열을 뽑아내기 위한 용도
    arr = [choice(string.ascii_letters) for _ in range(8)] # 무작위로 8글자를 뽑아줌
    pid = ''.join(arr)          # 파일 아이디생성
    extension = filename.split('.')[-1] # 파일이름으로부터 확장자명가져오기
    # ex) honux/asfqqwer.png
    return '%s/%s.%s' % (instance.owner.username, pid, extension)

class Photo(models.Model):
    image = models.ImageField(upload_to="blog/%Y/%m/%d") # 어디에 업로드할지 지정할 수 있음.
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)            # 하나의 사진은 한명의 사용자에게 속해야 하므로. 1:N의 관계
    thumname_image = models.ImageField()
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True) # 사용자가 입력하지 않고 업로드 하는 순간 자동으로 세팅이 됨. 
    profile_pic = models.ImageField(upload_to="blog/profile_pic")  
    

