from django.shortcuts import render
from .models import Post
# Create your views here.
def posta_list(request):
    posta_list=Post.objects.all()
    return render(request,"blog/posta_list.html", context={"postas": posta_list})

def home(request):
    return render(request,"blog/principal.html")