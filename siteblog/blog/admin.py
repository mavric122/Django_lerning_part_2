from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class Categorydmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, Categorydmin)
admin.site.register(Tags, TagAdmin)
admin.site.register(Post, PostAdmin)
