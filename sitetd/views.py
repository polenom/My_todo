from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import ToDoForm

# Create your views here.
def startPage(request):
    form = ToDoForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        print(user.get_session_auth_hash(), "HAST")


    return render(request, 'todo/startPage.html', {'form':form})


def test(request):
    print(request.user.is_authenticated, 77777777777777777777)
    print(request.session['_auth_user_id'], "SSESSION KEY")
    print(dir(request.session), "test")
    print(request.session.session_key)
    # logout(request)
    print(request.user.is_authenticated, 88888888888888888888)
    return render(request, 'todo/test.html')