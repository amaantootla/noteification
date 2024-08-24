from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import *

# Create your views here.

@login_required
def index(request):
    return render(request, 'app/index.html')


@login_required
def create_tag(request):
    pass


@login_required
def create_note(request):
    pass


@login_required
def get_tags(request):
    pass


@login_required
def get_notes(request):
    pass


@login_required
def get_tag(request, tag_id):
    pass


@login_required
def get_note(request, note_id):
    pass


@login_required
def update_tag(request, tag_id):
    pass


@login_required
def update_note(request, note_id):
    pass


@login_required
def delete_tag(request, tag_id):
    pass


@login_required
def delete_note(request, note_id):
    pass


def login_view(request):
    error = False

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            error = True

    return render(request, "app/login.html", {"error": error})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    error = False

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError:
            error = True
        else:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    
    return render(request, "app/register.html", {"error": error})