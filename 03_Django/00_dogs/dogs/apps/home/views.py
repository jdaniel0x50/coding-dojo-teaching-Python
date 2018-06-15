# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, "home/index.html")

def login(request):
    context = {
        "content": "login"
    }
    return render(request, "home/index.html", context)

def logout(request):
    context = {
        "content": "logout"
    }
    return render(request, "home/index.html", context)

