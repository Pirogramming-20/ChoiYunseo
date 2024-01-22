from django.shortcuts import render, redirect
from .models import Post, Like, DisLike
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    posts = Post.objects.all()
    ctx = {
        'posts' : posts
    }
    return render(request, 'posts/post_list.html', ctx)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)#아직 완전히 저장되기 전에 임시 객체로 불러옴
            post.user = request.user
            post.save()

            # Like 객체 생성, 연결
            like = Like(user=request.user, post=post)
            like.save()

            # DisLike 객체 생성, 연결
            dislike = DisLike(user=request.user, post=post)
            dislike.save()
            
            return redirect('posts:main')
        else:
            ctx = {
                'form' : form,#제대로된 폼이 아니니까 작성된 부분은 저장해서 다시 작성 페이지로 가기
            }
            return render(request, 'posts/post_create.html', ctx)
    elif request.method == 'GET':
        form = PostForm
        ctx = {
            'form' : form,
        }
        return render(request, 'posts/post_create.html', ctx)

def detail(request, pk):
    post = Post.objects.get(id=pk)
    ctx = {
        'post' : post,
    }
    return render(request, 'posts/post_detail.html', ctx)

def delete(request,pk):
    if request.method == "POST" :
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("posts:main")

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request) :
    req = json.loads(request.body)
    post_id = req['id']
    button_type = req['type']

    post = Post.objects.get(id=post_id)

    if button_type == 'likes_count':
        post.likes_count += 1
    else:
        post.dislikes_count += 1

    post.save()

    return JsonResponse({'id' : post_id, 'type' : button_type})

@csrf_exempt
def create_comment_ajax(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        content = request.POST.get('content')

        response_data = {
            'comment_id' : comment_id,
            'content':content,
        }
        return JsonResponse(response_data)