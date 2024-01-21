from django.shortcuts import render
from .forms import SignupForm
from django.contrib import auth

# Create your views here.
def main(request):#profile => 아이디, 올린 글, 좋아요 단 글, 댓글 단 내용
    pass

def signup(request):
    if request.method == "POST" :
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            

def login(request):
    pass

def logout(request):
    pass