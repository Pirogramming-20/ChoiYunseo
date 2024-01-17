from django.shortcuts import render,redirect
from .models import Idea
from .forms import IdeaForm

# Create your views here.
def main(request):
    sort_order = request.GET.get('sort', 'name')
    if sort_order == 'name':
        ideas = Idea.objects.order_by('title')
    elif sort_order == 'created':
        ideas = Idea.objects.order_by('created_at')
    elif sort_order == 'like':
        ideas = Idea.objects.order_by('-like')
    else:
        ideas = Idea.objects.all()
    # ideas = Idea.objects.all()
    ctx = {'ideas': ideas}
    return render(request, 'ideas/idea_list.html', ctx)

def create(request):
    if request.method == 'GET':
        form = IdeaForm()
        ctx = {'form': form}
        return render(request, 'ideas/idea_create.html', ctx)
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('ideas:main')

def detail(request, pk):
    idea = Idea.objects.get(id=pk)
    ctx = {'idea': idea}
    return render(request, 'ideas/idea_detail.html', ctx)

def delete(request, pk):
    if request.method == 'POST':
        Idea.objects.get(id=pk).delete()
    return redirect('ideas:main')

def update(request, pk):
    idea = Idea.objects.get(id=pk)
    if request.method == 'GET':
        form = IdeaForm(instance=idea)
        ctx = {'form': form, 'pk':pk}
        return render(request, 'ideas/idea_update.html', ctx)
    
    form = IdeaForm(request.POST, request.FILES, instance=idea)
    if form.is_valid():
        form.save()
    return redirect('ideas:detail', pk)

    