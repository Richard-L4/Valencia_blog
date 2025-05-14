from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    Model representing a category for blog posts.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField(default="No content")
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    # Add the ManyToManyField for categories
    categories = models.ManyToManyField(
        Category, related_name="posts", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    user = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)

    # remove the likes and dislikes attributes

    # See note on @property below
    def likes(self):
        return self.reactions.filter(reaction_type=1).count()

    def dislikes(self):
        return self.reactions.filter(reaction_type=0).count()


class Reaction(models.Model):
    REACTION_TYPES = (
        (0, "dislike"),
        (1, "like"),
    )

    reaction_type = models.IntegerField(choices=REACTION_TYPES)
    user = models.ForeignKey(
        User, related_name="reactions", on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, related_name="reactions", on_delete=models.CASCADE)
