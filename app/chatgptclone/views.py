from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def say_hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're using a ChatGPT Clone")