"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import blog.views
import account.views
import freeboard.views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = "home"),
    path('blog/<int:blog_id>', blog.views.detail_blog, name = "detail_blog"),
    path('upload/', blog.views.upload, name = "upload"),
    path('blog/new/', blog.views.new, name = "new"),
    path('blog/create/', blog.views.create, name = "create"),
    path('mypage', blog.views.mypage, name='mypage'),
    path('blog/postpage', blog.views.postpage , name = "postpage"),
    path('photo/<int:post_id>', blog.views.detail_post, name = "detail_post"),
    path('introduce/', blog.views.introduce, name = "introduce"),
    path('contact/', blog.views.contact, name = "contact"),
    path('deletephoto/<int:post_id>', blog.views.deletephoto, name='deletephoto'),
    path('deleteblog/<int:blog_id>', blog.views.deleteblog, name = 'deleteblog'),
    path('writecomment/<int:blog_id>', blog.views.writecomment_blog, name='writecomment_blog'),
    path('deletecomment/<int:blog_id>/<int:comment_id>', blog.views.deletecomment_blog, name='deletecomment_blog'),

    path('assign/', account.views.assign, name='assign'),
    path('login/', account.views.login, name='login'),
    path('logout/', account.views.logout, name='logout'),
    path('signup/', account.views.signup, name='signup'),
    path('signup/checkid/', account.views.checkid, name='checkid'),
    path('signup_1', account.views.signup_1 ,name = 'signup_1'),
    path('activate/<str:uid64>/<str:token>/', account.views.activate, name='activate'),
    
    # 게시판
    path('freeboard', freeboard.views.freeboard, name='freeboard'),
    path('freeboard/sort', freeboard.views.sort_freeboard, name='sort_freeboard'),
    path('freeboardSearch', freeboard.views.freeboardSearch, name='freeboardSearch'),
    path('freeboardSearch/sort', freeboard.views.sort_freeboardSearch, name='sort_freeboardSearch'),
    path('freeboard/newpost', freeboard.views.newpost, name='newpost'),
    path('createpost', freeboard.views.createpost, name='createpost'),
    path('deletepost/<int:post_id>', freeboard.views.deletepost, name='deletepost'),
    path('detail/<int:post_id>', freeboard.views.detail, name='detail'),
    path('writecomment/<int:post_id>', freeboard.views.writecomment, name='writecomment'),
    path('deletecomment/<int:post_id>/<int:comment_id>', freeboard.views.deletecomment, name='deletecomment'),
    path('editpost/<int:post_id>', freeboard.views.editpost, name='editpost'),
    path('edit/<int:post_id>', freeboard.views.edit, name='edit'),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)