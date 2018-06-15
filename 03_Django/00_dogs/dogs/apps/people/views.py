# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, "people/index.html")

def single_person(request, name):
    context = {
        "name": name,
    }
    return render(request, "people/index.html", context)