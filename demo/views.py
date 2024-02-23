from django.shortcuts import render

# Create your views here.
def showworld(request):
    return render(request,'demo/index.html')