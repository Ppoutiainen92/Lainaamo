from django.contrib import admin
from .models import Library


class LibraryAdmin(admin.ModelAdmin):
    save_as = True


# Register your models here.
admin.site.register(Library, LibraryAdmin)
