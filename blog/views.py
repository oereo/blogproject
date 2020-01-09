from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Blog
from .models import Comment
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def home(request):
    blogs = Blog.objects #쿼리셋 - 전달받은 객체 #메소드
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts' : posts})


    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
    return redirect('null')
    return render(request, 'home.html')
    # 입력받은 내용을 데이터 베이스에 넣어주는 함수


def mypage(request):
    user = request.user
    user_job=user.profile.job
    user_loc=user.profile.location
    user_name=user.username
    return render(request, 'mypage.html', {'name':user_name,'job':user_job, 'location':user_loc})


