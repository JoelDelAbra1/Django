from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import RoomForm

from .models import Room
# Create your views here.

def say_hello(request):
    return render(request, "hello.html")

def home(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request, "home.html", context)

def room(request, pk):#pk):
    #room = Room.objects.get(id=pk)
    context = {
        "room": room
    }
    return render(request, "room.html", context)

def create_room(request):
    
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST) # crea un formulario con los datos que se le pasan
        if form.is_valid(): # valida que los datos sean correctos
            form.save() # guarda en la base de datos
            return redirect("home") # redirecciona a la pagina home

    context = {'form': form}
    return render(request, "room_form.html", context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) # crea un formulario con los datos que se le pasan
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room) # crea un formulario con los datos que se le pasan
        if form.is_valid(): # valida que los datos sean correctos
            form.save() # guarda en la base de datos
            return redirect("home") # redirecciona a la pagina home

    context = {'form': form}
    return render(request, "room_form.html", context)

def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render (request, "delete.html", {'obj': room})