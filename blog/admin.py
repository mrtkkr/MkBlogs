from django.contrib import admin
from .models import Blog,Comment

# Register your models here.

admin.site.register(Comment)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=["title","author","created_date"]
    list_filter=["title","created_date"] #yana liste koyar
    list_display_links =["title","created_date"]
    search_fields=["title","content"] #arama çubuğu
    class Meta:
        model=Blog