# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, "dog/index.html")

def myview(request):
    return render(request, "dog/newpage.html")

def single_dog(request, id):
    context = {
        "id": id,
    }
    return render(request, "dog/index.html", context)

def create_dog(request):
    context = {
        "content": "create"
    }
    return render(request, "dog/index.html", context)

def edit_dog(request, id):
    context = {
        "content": "edit",
        "id": id,
    }
    return render(request, "dog/index.html", context)

def edit_second(request, id):
    context = {
        "content": "edit second time",
        "id": id,
    }
    return render(request, "dog/index.html", context)
    
def delete_dog(request, id):
    context = {
        "content": "delete",
        "id": id,
    }
    return render(request, "dog/index.html", context)
