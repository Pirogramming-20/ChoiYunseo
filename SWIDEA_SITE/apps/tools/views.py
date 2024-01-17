from django.shortcuts import render, redirect
from .models import Tool
from .forms import ToolForm
from apps.ideas.models import Idea
# Create your views here.

def tool_list(request):
    tools = Tool.objects.all()
    ctx = {'tools': tools}
    return render(request, 'tools/tool_list.html', ctx)

def create(request):
    if request.method == 'GET':
        form = ToolForm()
        ctx = {'form': form}
        return render(request, 'tools/tool_create.html', ctx)
    form=ToolForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('tools:list')

def detail(request, pk):
    tool = Tool.objects.get(id=pk)
    ideas = Idea.objects.all()
    related_ideas = []
    for idea in ideas:
        if idea.tool.title == tool.title:
            related_ideas.append(idea)

    ctx = {'tool' : tool,
           'related_ideas' : related_ideas}
    return render(request, 'tools/tool_detail.html', ctx)


def delete(request, pk):
    if request.method == 'POST':
        Tool.objects.get(id=pk).delete()
    return redirect('tools:list')

def update(request, pk):
    tool = Tool.objects.get(id=pk)
    if request.method == 'GET':
        form = ToolForm(instance=tool)
        ctx = {'form': form, 'pk': pk}
        return render(request, 'tools/tool_update.html', ctx)
    form = ToolForm(request.POST, instance=tool)
    if form.is_valid():
        form.save()
    return redirect('tool:detail', pk)