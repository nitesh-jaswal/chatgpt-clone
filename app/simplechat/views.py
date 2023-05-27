from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def get_answer(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")
    # return HttpResponse("Hello, world. You're using a ChatGPT Clone")