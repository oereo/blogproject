from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import JsonResponse


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['login']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print(user.username + " login")
            return redirect('/',user)
        else:
            return render(request, 'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_confirm']:
            user = User.objects.create_user(
                request.POST['username'],
                password = request.POST['password'],
                email = request.POST['email'],
                
            )
        user.profile.bio = request.POST['bio']
        print( user.profile.bio)
        auth.login(request,user)
        return redirect('/')
    return render(request,'signup.html')

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()    

def checkid(request):
    try:
        print(request.GET['username'])
        user = User.objects.get(username=request.GET['username'])
        print('user name is exist')
    except Exception as e:
        user= None
        print('user name is not exist')
    result = {
        'result' : 'success',
        'data' : 'not exist' if user is None else 'exist'
    }
    return JsonResponse(result)

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        print('log out success')
        return redirect('/')
    return render(request,'login.html')