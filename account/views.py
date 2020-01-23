from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage

from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token

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
                err=0
                user = User.objects.create_user(
                    request.POST['username'],
                    password = request.POST['password'],
                    email = request.POST['email'],
                    
                )
                user.profile.job = request.POST['job']
                user.profile.location = request.POST['location']
                user.profile.choose_people = request.POST['choose_people']
                user.is_active = False
                user.save()
                print( user.profile.job)
                print( user.profile.location)
                print( user.profile.choose_people)

                current_site = get_current_site(request) 
                    # localhost:8000
                message = render_to_string('user_activate_email.html',{
                        'user': user,
                        'domain': current_site.domain,
                        # 'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                        'token': account_activation_token.make_token(user),
                    })
                print(message)
                # auth.login(request,user)
                mail_subject = "[Munhwaparty] 회원가입 인증 메일입니다."
                user_email = user.email
                email = EmailMessage(mail_subject, message, to=[user_email])
                email.send()
                return render(request,'assignment.html')

                # return redirect('account:home')
        # return render(request, 'account/signup.html')
        else:
            err=1
            return render(request, 'signup.html',{'err' : err})

    return render(request, 'signup.html')

def assign(request):
    err=0
    if not request.POST.get('agree_a', None) == None:
     if not request.POST.get('agree_b', None) == None:
      return redirect('signup')
     else:
      return render(request, 'signup_1.html')
    else:
     return render(request, 'signup_1.html')





def activate(request, uid64, token):

    uid = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('/')
    else:
        return HttpResponse('비정상적인 접근입니다.')

def signup_1(request):
    return render(request, 'signup_1.html')    

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.job = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
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