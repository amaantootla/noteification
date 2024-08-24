from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .models import *

# Create your views here.


@login_required
def index(request):
    return render(request, 'app/index.html')


@csrf_exempt
@login_required
def create_tag(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    if not request.body:
        return JsonResponse({"error": "body is empty"}, status=400)
    
    data = json.loads(request.body)

    if data.get("name") is not None:
        name = data["name"]
    else:
         return JsonResponse({"error": "name is missing"}, status=400)
    
    if not name:
        return JsonResponse({"error": "name is empty"}, status=400)
    
    if len(name) > 64:
        return JsonResponse({"error": "name exceeds 64 character limit"}, status=400)

    try:
        Tag(name=name, owner=request.user).save()
    except IntegrityError:
        return JsonResponse({"error": f"Tag named \"{name}\" already exists"}, status=400)
    
    return JsonResponse({"message": f"Tag \"{name}\" created"}, status=201)

@csrf_exempt
@login_required
def create_note(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    if not request.body:
        return JsonResponse({"error": "body is empty"}, status=400)
    
    data = json.loads(request.body)

    if data.get("name") is not None:
        name = data["name"]
    else:
         return JsonResponse({"error": "name is missing"}, status=400)
    
    if data.get("content") is not None:
        content = data["content"]
    else:
        return JsonResponse({"error": "content is missing"}, status=400)
    
    # it is fine if content is empty, an empty note is valid
    if not name:
        return JsonResponse({"error": "name is empty"}, status=400)
    
    if len(name) > 64:
        return JsonResponse({"error": "name exceeds 64 character limit"}, status=400)

    try:
        Note(name=name, content=content, owner=request.user).save()
    except IntegrityError:
        return JsonResponse({"error": f"Note could not be made"}, status=400)
    
    return JsonResponse({"message": f"Note created"}, status=201)


@csrf_exempt
@login_required
def get_tags(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    data = {}
    for tag in Tag.objects.filter(owner=request.user):
        data[tag.id] = tag.name

    return JsonResponse(data, status=200)


@csrf_exempt
@login_required
def get_notes(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    data = [] # list of dicts
    for note in Note.objects.filter(owner=request.user):
        data.append({
            "id": note.id,
            "name": note.name,
            "content": note.content
        })

    return JsonResponse(data, safe=False, status=200)


@csrf_exempt
@login_required
def get_tag(request, tag_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    try:
        tag = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return JsonResponse({"error": "Tag does not exist"}, status=404)
    
    data = [] # first entry gives info on the tag, data[:1] gives all note ids that are associated with this tag
    data.append({
        "id": tag.id,
        "name": tag.name
    })

    for note in tag.notes.all():
        data.append({
            "note_id": note.id
        })

    return JsonResponse(data, safe=False, status=200)


@csrf_exempt
@login_required
def get_note(request, note_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    try:
        note = Note.objects.get(pk=note_id)
    except Note().DoesNotExist:
        return JsonResponse({"error": "Note does not exist"}, status=404)

    data = [] # same format as get_tag()
    data.append({
        "id": note.id,
        "name": note.name,
        "content": note.content
    })

    for tag in note.tags.all():
        data.append({
            "tag_id": tag.id
        })

    return JsonResponse(data, safe=False, status=200)      


@login_required
def update_tag(request, tag_id):
    pass


@login_required
def update_note(request, note_id):
    pass


@csrf_exempt
@login_required
def delete_tag(request, tag_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    try:
        tag = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return JsonResponse({"error": "Tag does not exist"}, status=404)

    tag.delete()
    return JsonResponse({"message": "Tag deleted"}, status=200)


@csrf_exempt
@login_required
def delete_note(request, note_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    try:
        note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        return JsonResponse({"error": "Note does not exist"}, status=404)

    note.delete()
    return JsonResponse({"message": "Note deleted"}, status=200)


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