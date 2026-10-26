from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def users_list(request):
    return HttpResponse("<h1> Users List </h1>")

def user_detail(request, username):
    clean_name = username.capitalize()
    return HttpResponse(f"<h1>User's name: {clean_name}</h1>")


def forum(request):
    return HttpResponse("<h1> Our forum </h1>")

def contacts(request):
    return HttpResponse("<h1> Contacts List </h1>")