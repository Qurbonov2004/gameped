from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def main(request):
    video_games=Video_games.objects.all()
    product=Product.objects.all()
    contact=Contact.objects.all()

    context={
        "video_game":video_games,
        "product":product,
        "contact":contact
    }

    # a=request.GET["name"]
    a=request.GET.get("Name")
    print(a)
    

    return render(request,"index.html",context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,"contact.html")

def product(request):
    return render(request,"product.html")


def remot(request):
    return render(request,"remot.html")


def video(request):
    return render(request,"video.html")

