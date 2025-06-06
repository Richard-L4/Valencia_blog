from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_protect


from .models import Post, Comment, CommentReaction
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

    comment_form = CommentForm()

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
        # Handle file upload if needed allow slug and title edit
        if form.is_valid():
            updated_post = form.save()
            return redirect('post_detail', slug=updated_post.slug)

    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, slug):
    """
    Delete an existing blog post if the user is the author.
    """
    post = get_object_or_404(Post, slug=slug)

    # Ensure that only the author of the post or an admin can delete it
    if post.author != request.user and not request.user.is_staff:
        messages.error
        (request, "You do not have permission to delete this post.")
        return redirect('post_detail', slug=slug)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('home')

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
    Custom reaction for the Reaction model.
    Prevents user's reacting more than once to a like or dislike.
    """
    if request.method == "POST":
        comment_id = request.POST.get("comment_id")
        action = request.POST.get("action")  # either 'like' or 'dislike'

        if action not in ['like', 'dislike']:
            return JsonResponse({'error': 'Invalid action'}, status=400)

        try:
            comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            return JsonResponse({'error': 'Comment not found'}, status=404)

        # Check for existing reaction by this user
        reaction, created = CommentReaction.objects.get_or_create(
            user=request.user,
            comment=comment,
            defaults={'reaction': action}
        )

        if not created:
            if reaction.reaction == action:
                return JsonResponse({'error': 'Already reacted'}, status=200)
            else:
                # User is switching their reaction
                if reaction.reaction == 'like':
                    comment.likes -= 1
                else:
                    comment.dislikes -= 1

                reaction.reaction = action
                reaction.save()

        # Apply the new reaction
        if action == 'like':
            comment.likes += 1
        elif action == 'dislike':
            comment.dislikes += 1

        comment.save()

        return JsonResponse({
            'likes': comment.likes,
            'dislikes': comment.dislikes,
            'message': 'Reaction updated successfully'
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
