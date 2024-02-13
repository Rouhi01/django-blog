from django.contrib import admin
from .models import Category, Blog, Comment



@admin.register(Blog)
class moAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}
    list_display = ['title', 'category', 'author', 'status', 'is_featured']
    search_fields = ['id', 'title', 'category__category_name', 'status']
    list_editable = ['is_featured']


admin.site.register(Comment)
admin.site.register(Category)