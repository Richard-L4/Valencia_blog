from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
    A form for users to submit collaboration requests.

    This form is linked to the CollaborateRequest model and includes
    fields for the user's name, email, and message.
    """
    class Meta:
        # Connect this form to the CollaborateRequest model
        model = CollaborateRequest

        # Specify which fields from the model to include in the form
        fields = ('name', 'email', 'message')