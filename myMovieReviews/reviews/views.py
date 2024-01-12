from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def reviews_list(request):
    reviews = Review.objects.all()
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

def reviews_create(request):
    if request.method == "POST":
        Review.objects.create(
            title = request.POST["title"],
            release_year = request.POST["release_year"],
            genre = request.POST["genre"],
            star_score = request.POST["star_score"],
            running_time = request.POST["running_time"],
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
        review.running_time = request.POST["running_time"]
        review.content = request.POST["content"]
        review.director = request.POST["director"]
        review.actor = request.POST["actor"]
        review.save()
        return redirect(f"/reviews/{pk}")
    
    context = {
        "review" : review
    }
    return render(request, "reviews_update.html", context)

def reviews_delete(request, pk):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/reviews")