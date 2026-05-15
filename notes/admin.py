
# Register your models here.

from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Note,NoteAdmin)