from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_title', 'rating', 'user', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('movie_title', 'content', 'user__username')
