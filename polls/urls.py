from django.urls import path
from . import views

# Add possible urls within polls/
urlpatterns = [
    path('', views.index, name='index') # '' denotes home/index page --> "polls/"
]
