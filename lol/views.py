from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "PAGINA SOBRE LETI LA MAS HERMOSA"}
    return render(request, "lol/index.html", context)