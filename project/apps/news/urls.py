from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListCreate.as_view()),
]
