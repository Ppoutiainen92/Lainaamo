from django.contrib import admin
from .models import Library, LibraryBook


class LibraryAdmin(admin.ModelAdmin):
    save_as = True


# Register your models here.
admin.site.register(Library, LibraryAdmin)
admin.site.register(LibraryBook, LibraryAdmin)
