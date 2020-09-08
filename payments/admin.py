from django.contrib import admin
from .models import *


class Admin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Policyholder)