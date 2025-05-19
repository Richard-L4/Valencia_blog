"""
Forms for blog comments and custom signup form for user registration.

Includes:
- CommentForm for submitting blog post comments.
- CustomSignupForm that customizes the signup process
and removes password help texts.
"""

from django import forms
from .models import Comment, Post
from allauth.account.forms import SignupForm


class PostForm(forms.ModelForm):
    """
    Form for creating and updating Post instances.
    """
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content',
                  'status', 'featured_image', 'excerpt']


class CommentForm(forms.ModelForm):
    """
    Form for users to submit a comment.
    This form is linked to the Comment model and allows users
    to input their comment body.
    """
    class Meta:
        model = Comment
        fields = ('body',)


class CustomSignupForm(SignupForm):
    """
    Custom signup form to override default field labels and remove help texts.
    """
    def __init__(self, *args, **kwargs):
        """Initialize the form and customize field labels and help texts."""
        super().__init__(*args, **kwargs)

        # Customize field labels
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email (optional)"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Password (again)"

        # Remove password help texts
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
