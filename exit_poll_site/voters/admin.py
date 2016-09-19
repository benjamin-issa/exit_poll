from django.contrib import admin

# Register your models here.
from .models import Voter, Phone

admin.site.register(Voter)
admin.site.register(Phone)