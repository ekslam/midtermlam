from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostModelForm
from datetime import datetime

def index(request):
    content = {}
    post = Post.objects.all()
    content['post'] = post
    #context['questions'] = questions
    if request.is_ajax:
        return render(request,'index.html',content)
    else:
        return HttpResponse(status=400)

def detail(request, post_id):
    content = {}
    content['post'] = Post.objects.get(id = post_id)
    content['comment'] = Post.objects.all()


def create(request):
    content = {}
    content['form'] = PostModelForm(initial={'date_created' : datetime.now()})
    if request.method == 'POST':
        form = ContentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/post/')
        else:
            content['form'] = form
            render(request, 'create.html', context)
    else:
        return render(request, 'create.html', context)


def update(request):
    content = {}
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return HttpResponse('Post updated')
        else:
            content['form'] = form
            render(request, 'update.html', content)
    else:
        #question = Question.objects.get(id=question_id)
        content['form'] = PostModelForm(instance=post)
        #context['q_id'] = question_id
    return render(request, 'update.html', content)

def comment(request, post_id):
    content = {}
    if request.method == 'POST':
        content['form'] = PostModelForm(initial={'date_created' : datetime.now()})
        render(request, 'detail.html', content)
