from django.urls import path
from lol import views
urlpatterns = [
    path("", views.index , name="index")    
]