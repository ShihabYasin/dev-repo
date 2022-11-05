from django.urls import path, include
from . import views
urlpatterns = [
    path("home/",  views.home_view, name="homepage-url"),
    path("index/",  views.home_view, name="indexpage-url"),
]