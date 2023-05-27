from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_answer, name="index"),
]