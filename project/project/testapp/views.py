from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import *


def upload_file(request):
    wordcount = request.POST.get("wordcount")
    action = request.POST.get("action")
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("upload")
    else:
        form = UploadFileForm()

    if action == "delete":
        Document.objects.all().last()

    return render(request, "upload.html", {"form": form})
