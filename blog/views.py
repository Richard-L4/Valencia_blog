from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_protect


from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Public view: shows a list of published posts on the homepage.
    GET requests can be viewed by everyone, but POST requests are protected.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual post with comments.

    Handles GET and POST requests:
    - GET requests display the post and its comments.
    - POST requests allow the user to submit a comment (if logged in).
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        if request.user.is_authenticated:
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
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'You must be logged in to comment'
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
            "categories": post.categories.all(),
        },
    )


@login_required
def edit_post(request, slug):
    """
    Edit an existing blog post if the user is the author.
    """
    post = get_object_or_404(Post, slug=slug)

    # Ensure that only the author of the post or an admin can edit it
    if post.author != request.user and not request.user.is_staff:
        messages.error
        (request, "You do not have permission to edit this post.")
        return redirect('post_detail', slug=slug)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        # Handle file upload if needed
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=slug)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Ensure that only the author of the post or an admin can delete it
    if post.author != request.user and not request.user.is_staff:
        messages.error
        (request, "You do not have permission to delete this post.")
        return redirect('post_detail', slug=slug)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('home')  # Replace with your homepage URL name

    return render(request, 'blog/delete_post.html', {'post': post})


@login_required
def comment_edit(request, slug, comment_id):
    """
    Edit an existing comment if the user is the author.

    This view ensures that only the author of the comment
    can edit it. If the form is valid,
    the comment is updated, and the post is marked as needing approval.
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)

        if comment.author == request.user or request.user.is_staff:
            # Ensure only author or admin can edit
            comment_form = CommentForm(data=request.POST, instance=comment)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.approved = False
                comment.save()
                messages.add_message(
                    request, messages.SUCCESS, 'Comment Updated!')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Error updating comment!'
                )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'You can only edit your own comments!'
            )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    Delete an existing comment if the user is the author.

    This view ensures that only the author of the comment
    can delete it.
    If successful, a success message is displayed; otherwise,
    an error message is shown.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user or request.user.is_staff:
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

    The user must be authenticated, and the request must be a POST request.
    If the comment is found and the action is valid, the like/dislike count
    is updated.
    """
    if request.method == "POST" and request.user.is_authenticated:
        comment_id = request.POST.get("comment_id")
        action = request.POST.get("action")

        try:
            comment = Comment.objects.get(pk=comment_id)

            if action == "like":
                comment.likes += 1
            elif action == "dislike":
                comment.dislikes += 1

            comment.save()

            return JsonResponse({
                'likes': comment.likes,
                'dislikes': comment.dislikes
            })

        except Comment.DoesNotExist:
            return JsonResponse({'error': 'Comment not found'}, status=404)

    return JsonResponse({'error': 'Invalid request'}, status=400)
