from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.
def profile(request):#profile => 아이디, 올린 글, 좋아요 단 글, 댓글 단 내용
    user = request.user
    if user.is_authenticated:
        ctx={
            'user':user
        }
        return render(request, 'users/user_profile.html', ctx)
    return redirect('users:login')

def signup(request):
    if request.method == "POST" :
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save() #form으로 생성된 유저 객체는 user 변수에 저장됨
            auth.login(request, user) #장고 인승 시스템을 사용하여 사용자를 로그인하는 코드 => 로그인 상태를 유지
            return redirect('posts:main') 
        else:
            ctx={
                'form':form,
            }
            return render(request, 'users/user_signup.html', ctx)
    else:
        form=SignupForm()
        ctx={
            'form':form,
        }
        return render(request, 'users/user_signup.html', ctx)  

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('users:profile')
        else:
            ctx = {
                'form' : form,
            }
            return render(request, 'users/user_login.html', ctx)
    else:
        form = AuthenticationForm()
        ctx = {
            'form' : form,
        }
        return render(request, 'users/user_login.html', ctx)

def logout(request):
    auth.logout(request)
    return redirect('posts:main')