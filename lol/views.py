from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Prueba django"}
    return render(request, "lol/index.html", context)