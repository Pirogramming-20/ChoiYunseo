from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def reviews_list(request):
    reviews = Review.objects.order_by('-star_score')
    context = {
        "reviews" : reviews,
    }
    return render(request, 'reviews_list.html', context)

def reviews_read(request, pk):
    review = Review.objects.get(id = pk)
    context = {
        "review" : review,
    }
    return render(request, "reviews_read.html", context)

def cal_running_time(request):
    try:
        all_running_time = int(request.POST["running_time"])
        running_time_hour = all_running_time//60
        running_time_minute = all_running_time%60
        running_time = f"{running_time_hour}시간 {running_time_minute}분"
    except (KeyError, ValueError):
        running_time = request.POST["running_time"]
    return running_time

def reviews_create(request):
    if request.method == "POST":
        Review.objects.create(
            title = request.POST["title"],
            release_year = request.POST["release_year"],
            genre = request.POST["genre"],
            star_score = request.POST["star_score"],
            running_time = cal_running_time(request),
            content = request.POST["content"],
            director = request.POST["director"],
            actor = request.POST["actor"],
        )
        return redirect("/reviews")
    return render(request, "reviews_create.html")

def reviews_update(request, pk):
    review = Review.objects.get(id=pk)
    if request.method == "POST" :
        review.title = request.POST["title"]
        review.release_year = request.POST["release_year"]
        review.genre = request.POST["genre"]
        review.star_score = request.POST["star_score"]
        all_running_time = request.POST["running_time"]
        review.running_time = cal_running_time(request)
        review.content = request.POST["content"]
        review.director = request.POST["director"]
        review.actor = request.POST["actor"]
        review.save()
        return redirect(f"/reviews/{pk}")
    
    context = {
        "review" : review,
    }
    return render(request, "reviews_update.html", context )

def reviews_delete(request, pk):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/reviews")