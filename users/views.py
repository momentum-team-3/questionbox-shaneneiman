from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionBoxUserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def create_user(request):
    if request.method == "GET":
        form = QuestionBoxUserCreationForm()
    else:
        form = QuestionBoxUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="list_questions")
    return render(request, "users/create_user.html", {"form": form})


def login_user(request):
    retry = False
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(to="list_questions")
        else:
            retry = True
    return render(request, "users/login_user.html", {"retry": retry})


def logout_user(request):
    logout(request)
    return redirect("list_questions")
