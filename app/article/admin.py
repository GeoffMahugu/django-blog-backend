from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    exclude = ['slug']

admin.site.register(Article, ArticleAdmin)
