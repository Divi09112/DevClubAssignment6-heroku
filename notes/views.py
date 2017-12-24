from django.shortcuts import render
from .models import todo
from .forms import ToDoCreate, SignUp
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/notes/login/')
def notes(request):
    tasks =todo.objects.filter(user=request.user)
    return render(
        request,
        'notes.html',
        context={'tasks':tasks,}
)

def welcome(request):
    return render(
        request,'welcome.html'
)

def create_todo(request):
    tasks=todo.objects.all()
    if request.method=='POST':
        form = ToDoCreate(request.POST)
        title = request.POST.get('title')
        content = request.POST.get('content')
        user=request.user
        task=todo(title=title,content=content,user=user)
        task.save()
        return HttpResponseRedirect(reverse('notes'))
    else:
       form = ToDoCreate()

    return render(request, 'notes/create_todo.html', {'form':form,'tasks':tasks})

def create_user(request):
    if request.method=='POST':
        form=SignUp(request.POST)
        if form.is_valid():
            form.save()
            uname=form.cleaned_data['username']
            pword=form.cleaned_data['password1']
            user=authenticate(username=uname,password=pword)
            login(request, user)
            return HttpResponseRedirect(reverse('notes'))
    else:
        form =SignUp()
    return render(
        request,'notes/signup.html',{ 'form':form }
)

@login_required(login_url='/notes/login/')
def show(request,pk):
    tasks = todo.objects.filter(user=request.user)
    try:
        taskshow=todo.objects.get(pk=pk)
    except todo.DoesNotExist:
        raise Http404("Task does not exist")

    return render(
        request,
        'notes/show.html',
        context={'taskshow':taskshow, 'tasks':tasks}
)
