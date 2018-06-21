# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import date               # important! -- add this import statement

def view_user(request, user_id):        # user_id will come from the urls.py route
    user = User.objects.get(id=user_id) # get the user object
    today_date = date.today()                # get today's date

    context = {                         # store the variables in the context dictionary
        "user": user,                   # keys are in strings
        "today": today_date,            # values are usually variables defined in other places
    }                                   # DON'T FORGET THE COMMA AFTER EACH LINE !!!!!!
                                        # pass in the context dictionary to the render function
    return render(request, "my_app/view_user.html", context)

