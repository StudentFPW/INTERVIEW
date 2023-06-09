from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import *
import string


def upload_file(request):
    wordcount = request.POST.get("wordcount")
    action = request.POST.get("action")
    files = Document.objects.all()
    current_file = Document.objects.all().values().last()["docfile"]
    characters = string.punctuation
    word_cnt = 0

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()

    if files:
        direct = files.values().last()["docfile"]
        with open(f"media/{direct}", encoding="utf-8") as file:
            for words in file:
                for word in words.split():
                    if word in characters:
                        continue
                    if word.lower() == wordcount:
                        word_cnt += 1

    if action == "delete":
        if files:
            Document.objects.all().last().delete()
        else:
            return render(request, "empty.html")

    context = {
        "form": form,
        "word_cnt": word_cnt,
        "files": files,
        "current_file": current_file,
    }

    return render(request, "upload.html", context)
