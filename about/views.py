from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    View to display the 'About Me' page and
    handle collaboration form submissions.
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(
                request,
                "Collaboration request received! I aim"
                " to respond within 5 working days."
            )
            return redirect("about")

    else:
        collaborate_form = CollaborateForm()

    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )
