from django.urls import path
from blog import views
urlpatterns = [
    path("", views.posta_list, name="posta_list"),
    
    
]