from django.contrib import admin
from rango.models import Category, Page

class PageDisplay(admin.ModelAdmin):
    list_display = ('title','category','url')

admin.site.register(Category)
admin.site.register(Page, PageDisplay)