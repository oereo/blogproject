from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Blog
from .models import Comment
from .models import Photo
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UploadForm
from django.views.generic.list import ListView

# Create your views here.

def home(request):
        user = request.user
        blogs = Blog.objects #쿼리셋 - 전달받은 객체 #메소드
        blog_list = Blog.objects.all().order_by('-id')
        paginator = Paginator(blog_list, 3)
        page = request.GET.get('page')
        page_blogs = paginator.get_page(page)
        imagePost= Photo.objects.all()
        if user.is_staff == True:   
            return render(request, 'home.html', {'page_blogs' : page_blogs, 'imagePost':imagePost})
        else:
            return render(request, 'home_user.html', {'page_blogs' : page_blogs, 'imagePost':imagePost})    
   



    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드
def detail_blog(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    blog_detail.increaseViews()

    return render(request, 'detail_blog.html', {'blog_detail':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    user = request.user
    blog = Blog()
    blog.user_id = user.id
    blog.owner = user.username
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    # return redirect('/blog/'+str(blog.id))
    return redirect('home')
   
    # 입력받은 내용을 데이터 베이스에 넣어주는 함수


def mypage(request):
    user = request.user
    if user.is_staff == False:
        user_job=user.profile.job
        user_loc=user.profile.location
        user_name=user.username
        email=user.email
        return render(request, 'mypage.html', {'name':user_name,'job':user_job, 'location':user_loc, 'email':email})
    else:
        users =  User.objects.all()
        user_job=user.profile.job
        user_loc=user.profile.location
        user_name=user.username
        return render(request, 'staff_page.html', {'name':user_name,'job':user_job, 'location':user_loc, 'user_data':users})


def upload(request):
   
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES) # 대용량인 이미지를 처리해야 하므로 두 매개변수를 넘겨줘야함.
        if form.is_valid():
            photo = form.save(commit=False) # photo객체를 가져오긴 하나 DB에 아직 저장하진 않음
            photo.owner = request.user      # request.user는 로그인한 사용자
            form.save()
            return render(request, 'home.html', {'form' : form})
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form' : form})      

# def upload(request):
#     form = UploadDocumentForm()
#     if request.method == 'POST':
#         form = UploadDocumentForm(request.POST, request.FILES)  # Do not forget to add: request.FILES
#         if form.is_valid():
#             # Do something with our files or simply save them
#             # if saved, our files would be located in media/ folder under the project's base folder
#             form.save()
#     return render(request, 'upload.html', locals())

class HomeView(ListView):
    # model = Photo 이렇게 해주면 사용자를 안가리고 모든 photo객체가 넘어가게 되므로 아래와 같이 쿼리를 지정해줌.
    context_object_name = 'user_photo_list' # 템플릿에 전달되는 이름

    def get_queryset(self):
        user = self.request.user    # 로그인되어있는 사용자
        return user.photo_set.all().order_by('-pub_date')