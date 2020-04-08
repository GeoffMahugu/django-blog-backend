from django.contrib import admin
from .models import Author

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    model = Author
    exclude = ['slug']

admin.site.register(Author, AuthorAdmin)
