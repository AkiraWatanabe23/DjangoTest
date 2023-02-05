from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#ユーザーに表示するものを記述する(関数で定義する)

def index(request):
    return render(request, "hello/index.html")

def brain(request):
    return HttpResponse("Good morning!!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })