# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

US_STATES = [
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DE",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY"
]

class DojoManager(models.Manager):
    def create_error_message(self, label, message):
        error = {}
        error["label"] = label
        error["message"] = message
        return error, False

    def validate(self, form_data):
        data_is_valid = True
        errors = []

        if len(form_data['name']) < 2:
            error, data_is_valid = self.create_error_message(
                "name",
                "Name is required and should be at least two characters"
            )
            errors.append(error)

        if len(form_data['name']) > 100:
            error, data_is_valid = self.create_error_message(
                "name",
                "Name must be less than 100 characters"
            )
            errors.append(error)
        
        if len(form_data['city']) < 2:
            error, data_is_valid = self.create_error_message(
                "city",
                "City is required and should be at least two characters"
            )
            errors.append(error)
        
        if len(form_data['city']) > 50:
            error, data_is_valid = self.create_error_message(
                "city",
                "City must be less than 50 characters"
            )
            errors.append(error)
        
        if not re.match(r'^[a-zA-Z.\s]+$', form_data['city']):
            error, data_is_valid = self.create_error_message(
                "city",
                "City has invalid characters"
            )
            errors.append(error)
        
        if form_data['state'] not in US_STATES:
            error, data_is_valid = self.create_error_message(
                "state",
                "State must be a US state"
            )
            errors.append(error)
            

        if len(form_data['state']) != 2:
            error, data_is_valid = self.create_error_message(
                "state",
                "State is required and must be exactly two characters"
            )
            errors.append(error)
        return data_is_valid, errors

class Dojo(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = DojoManager()

