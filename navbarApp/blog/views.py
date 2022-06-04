from urllib import request
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
# Create your views here.

database = {
    "blogs":[
        {
        "id":123,
        "img":"python.jpg",
        "description":"The best Programming language and using for ML, AI, Web Development, Data Science etc.",
        "name" : "Python"
    },
    {
        "id":124,
        "img":"C#.jpg",
        "description":"The best Programming language and using for Web Development, App development, Game Development etc.",
        "name" : "C#"
    },
    {
        "id":125,
        "img":"java.jpg",
        "description":"The best Programming language and using for App development Web Development, Game Development, Big Data etc.",
        "name" : "Java"
    },
    {
        "id":126,
        "img":"django.jpg",
        "description":"The best Python FrameWork using for Web App development and Easy to learn",
        "name" : "Django"
    }
    ]
}

def main(request):
    context = {
        "blogs" : database["blogs"]
    }
    # print(type(context))
    return render(request,'blog/main_page.html')

def blog(request):
    context = database
    return render(request,'blog/blog.html',context)
def about(request):
    context = database.get("blogs")
    return render(request,"blog/about.html")
