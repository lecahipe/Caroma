
from django.contrib import admin
from data.models import *
from django.apps import apps

# Get all models in the app
models = apps.get_models()

# Register all models for admin site
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
