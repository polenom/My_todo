from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, models
from .forms import ToDoForm, RegisterForm, createTodo
from .models import *
import json
from django.utils import timezone
from django.core.paginator import  Paginator, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def startPage(request):
    forms = ToDoForm()
    print(type(request))
    statuserr = False
    if request.user.is_authenticated:
        return redirect('/todo')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/todo')
        else:
            statuserr = True
        # print(user.get_session_auth_hash, "HAST")


    return render(request, 'todo/startPage.html', {'forms':forms, "statuserr": statuserr})

def registerUser(request):
    forms = RegisterForm()
    statuserr = False

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if not User.objects.filter(username=username).exists():
            user =User.objects.create_user(username, email, password)
            user.save()
            forms = ToDoForm()
            return redirect("/")
        statuserr = True
    return render(request, "todo/register.html", {"forms":forms, "statuserr": statuserr})

def pageToDo(request):
    if request.user.is_authenticated:
        forms = createTodo()
        username = request.user
        # todos = UserToDo.objects.filter(username = username, status=True)
        tentodos = User.objects.get(username=request.user).userToDo.all().order_by('-timeCreate')[:10]

        truetodos = UserToDo.objects.filter(username = username, status=True).order_by('-timeCreate')

        falsetodos = UserToDo.objects.filter(username = username, status=False).order_by('-timeCreate')
        paginator = Paginator(truetodos, 5)
        paginator2 = Paginator(falsetodos,5)
        pageNum = request.GET.get('page')
        pageNum2 = request.GET.get('page2')
        listtd = request.GET.get('list')

        try:
            truetodos = paginator.page(pageNum)
        except PageNotAnInteger:
            truetodos = paginator.page(1)
        try:
            falsetodos = paginator2.page(pageNum2)
        except PageNotAnInteger:
            falsetodos = paginator2.page(1)

        if request.method == "POST":
            username = User.objects.get(pk=request.user.pk)
            title = request.POST['title']
            text = request.POST['text']
            status = True if request.POST.get('status') else False
            timeCreate = timezone.now()
            newToDo = UserToDo(username=username, title=title, text=text, status=status, timeCreate=timeCreate)
            newToDo.save()
            return redirect('/todo')
    return render(request, "todo/userPage.html", {'truetodos':truetodos,'falsetodos':falsetodos, 'forms':forms, 'username': request.user,'listtd': listtd, 'tentodos':tentodos})

def pageoneToDo(request, pk):
    if request.user.is_authenticated:
        try:
            form = UserToDo.objects.get(username=request.user, pk=pk)
        except:
            form = False
        if request.method == "POST" and form:
            text = request.POST.get('text')
            if text != form.text and text:
                form.text = text
                form.save()
            form.status = True if request.POST.get('status') else False
            form.save()
            return  redirect('/todo')
        if form:
            return render(request, 'todo/pageoneToDo.html', {'form':form})
    return HttpResponse('mistake 404')


def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')


def deletetodo(request):
    if request.user.is_authenticated:
        username = User.objects.get(pk=request.user.pk)
        todo = username.userToDo.filter(pk=request.GET.get('pk'))
        if todo:
            todo.delete()
    return pageToDo(request)


@csrf_exempt
def checkUserName(request):
    status = False
    if request.method == "POST":
        username = json.loads(request.body)['username']
        if not User.objects.filter(username=username):
            status = True
    return JsonResponse({'status': status})


def test(request):
    print(request.user.is_authenticated, 77777777777777777777)
    print(request.session['_auth_user_id'], "SSESSION KEY")
    print(dir(request.session), "test")
    print(request.session.session_key)
    # logout(request)
    print(request.user.is_authenticated, 88888888888888888888)
    return render(request, 'todo/test.html')