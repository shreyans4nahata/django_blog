from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
class entryadmin(MarkdownModelAdmin):
	list_display = ("title","created")
	prepopulated_fields = {"slug":("title",)}

admin.site.register(models.entry,entryadmin)
admin.site.register(models.Tag)
# Register your models here.
