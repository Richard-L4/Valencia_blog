from django.db import models
from cloudinary.models import CloudinaryField

# Models for the 'about' app


class About(models.Model):
    """
    Stores information about the site or
    individual, typically for an About page.
    Includes a title, an image, the main content, and a timestamp for updates.
    """
    title = models.CharField(max_length=200)  # Title of the about section
    updated_on = models.DateTimeField(auto_now=True)
    # Automatically updates the timestamp on save
    profile_image = CloudinaryField('image', default='placeholder')
    # Image field stored via Cloudinary
    content = models.TextField()  # Main text content of the about section

    def __str__(self):
        return self.title  # Returns the title when the object is printed


class CollaborateRequest(models.Model):
    """
    Represents a request from a user who wants to collaborate.
    Includes name, email,
    message, and a flag to indicate if the request has been read.
    """
    name = models.CharField(max_length=200)
    # Name of the person submitting the request
    email = models.EmailField()  # Email address of the requester
    message = models.TextField()  # Message or collaboration details
    read = models.BooleanField(default=False)
    # Whether the request has been read

    def __str__(self):
        return f"Collaboration request from {self.name}"
        # Readable representation of the object