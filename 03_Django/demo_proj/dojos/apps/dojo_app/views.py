# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *

def index(request):
    dojos = Dojo.objects.all()

    context = {
        "dojos" : dojos,
    }
    return render(request, "dojo_app/index.html", context)

def new_get(request):
    print("*"*50)
    print("In New_Get Method")
    if "errors" in request.session:
        errors = request.session["errors"]
    else:
        errors = []
    
    print(errors)

    context = {
        "errors": errors
    }
    return render(request, "dojo_app/new.html", context)

def create_post(request):
    data_is_valid, errors = Dojo.objects.validate(request.POST)
    if data_is_valid:
        dojo = Dojo.objects.create(
            name=request.POST["name"],
            city=request.POST["city"],
            state=request.POST["state"]
        )
        return redirect('/dojos')
    else:
        request.session["errors"] = errors
        return redirect('/dojos/new')

