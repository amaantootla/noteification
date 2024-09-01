from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.


def all_notes(user):
    return Note.objects.filter(owner=user).order_by('-last_updated')


def all_folders(user):
    return Folder.objects.filter(owner=user)


@login_required(login_url='/login')
def delete_note(request, note_id, parent):

    # https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/#get-object-or-404
    note = get_object_or_404(Note, pk=note_id)
    
    if request.user != note.owner:
        return HttpResponseForbidden("Ownership Error.")

    note.delete()

    return HttpResponseRedirect(reverse(parent)) # janky solution, not that a page that does not exist can even be reached


def delete_folder(user, folder_id):
    pass


@login_required(login_url='/login')
def index(request):
    return render(request, "app/index.html", {
        "notes": all_notes(request.user),
        "folders": all_folders(request.user)
    })


def login_view(request):
    message = None

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:     
            message = "Invalid username and/or password."

    return render(request, "app/login.html", {"message": message})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    message = None

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError:
                message = "Username already taken."
        else:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    
    return render(request, "app/register.html", {"message": message})