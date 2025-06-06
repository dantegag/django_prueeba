from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "bienvenido a mi app"}
    return render(request, "lol/index.html", context)