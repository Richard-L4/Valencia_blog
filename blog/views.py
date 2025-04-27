from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
@csrf_protect
def update_reaction(request):
    """
    Handle POST requests to update the like or dislike count for a comment.

    This view expects a POST request containing:
    - 'comment_id': the ID of the comment to update
    - 'action': a string, either 'like' or 'dislike'

    It ensures the user is authenticated and the
    request is protected against CSRF.
    If the comment is found and the action is valid,
    it updates the corresponding field
    and returns the new counts as JSON.
    Returns:
        JsonResponse: Updated like/dislike counts if successful,
                      or an error message with appropriate HTTP status.
    """
    # Ensure the request is a POST and the user is authenticated
    if request.method == "POST" and request.user.is_authenticated:
        comment_id = request.POST.get("comment_id")
        action = request.POST.get("action")

        try:
            # Try to retrieve the comment by ID
            comment = Comment.objects.get(pk=comment_id)

            # Update the appropriate counter based on the action
            if action == "like":
                comment.likes += 1
            elif action == "dislike":
                comment.dislikes += 1

            # Save the updated comment
            comment.save()

            # Return the updated counts
            return JsonResponse({
                'likes': comment.likes,
                'dislikes': comment.dislikes
            })

        except Comment.DoesNotExist:
            # Return a 404 error if the comment was not found
            return JsonResponse({'error': 'Comment not found'}, status=404)

    # Return a 400 error for invalid requests (non-POST or unauthenticated)
    return JsonResponse({'error': 'Invalid request'}, status=400)
