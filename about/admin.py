from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model.
    Uses Summernote for the 'content' field to allow rich text editing.
    """
    summernote_fields = ('content',)


# Note: SummernoteModelAdmin is used above to integrate the Summernote
#       WYSIWYG editor.

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CollaborateRequest model.
    Displays message and read status in the admin list view.
    """
    list_display = ('message', 'read',)
