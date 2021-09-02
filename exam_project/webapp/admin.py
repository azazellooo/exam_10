from django.contrib import admin

from webapp.models import Category, Advert


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']
    list_filter = ['category_name']
    fields = ['category_name']


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'author', 'is_moderated', 'published_at']
    list_filter = ['author', 'created_at', 'is_moderated', 'is_rejected']
    fields = ['title', 'description', 'picture', 'author', 'price', 'category', 'is_moderated', 'is_rejected']
    readonly_fields = ['created_at', 'id']


# Register your models here.
