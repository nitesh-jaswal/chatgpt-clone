from django.urls import path

from . import views

app_name = 'simplechat'

urlpatterns = [
    path("", views.letschat, name="chat"),
    path("get_answer", views.get_answer, name="get_answer"),
]