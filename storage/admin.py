from django.contrib import admin

# Register your models here.
from storage.models import GeneratedGraph

admin.site.register(GeneratedGraph)
