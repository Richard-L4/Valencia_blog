from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Admin configuration for the Post model using Summernote for rich text editing
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Custom admin interface for the Post model.
    Uses Summernote for rich text editing of the 'content' field.
    """

    # Fields to display in the list view of posts
    list_display = ('title', 'slug', 'status', 'created_on')

    # Enables search functionality on the 'title' and 'content' fields
    search_fields = ['title', 'content']

    # Adds filter sidebar for 'status' and 'created_on' fields
    list_filter = ('status', 'created_on')

    # Automatically populates the 'slug' field based on the 'title'
    prepopulated_fields = {'slug': ('title',)}

    # Enables Summernote editor on the 'content' field
    summernote_fields = ('content',)


# Registers the Comment model with the default admin interface
admin.site.register(Comment)