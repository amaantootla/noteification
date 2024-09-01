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


@login_required(login_url='/login')
def createdit_note(request, note_id, parent):
    if note_id != 0:
        note = get_object_or_404(Note, pk=note_id)

        if note.owner != request.user:
            return HttpResponseForbidden("Ownership Error.")
    else:
        note = Note(owner=request.user, body='')
        note.save()
        note_id = note.id

    if request.method == "POST":
        note.body = request.POST["body"]
        note.save()
        return HttpResponseRedirect(reverse(parent))
    
    return render(request, "app/edit.html", {
        "id": note_id,
        "body": note.body
    })


@login_required(login_url='/login')
def delete_note(request, note_id, parent):
    # https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/#get-object-or-404
    note = get_object_or_404(Note, pk=note_id)
    
    if request.user != note.owner:
        return HttpResponseForbidden("Ownership Error.")

    note.delete()
    return HttpResponseRedirect(reverse(parent)) # janky solution


@login_required(login_url='/login')
def index(request):
    return render(request, "app/index.html", {
        "notes": all_notes(request.user),
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