from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import *
import string


def upload_file(request):
    wordcount = request.POST.get("wordcount")
    action = request.POST.get("action")
    file = Document.objects.all()
    characters = string.punctuation
    word_cnt = 0

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()

    if file:
        direct = file.values().last()["docfile"]
        with open(f"media/{direct}", encoding="utf-8") as file:
            for words in file:
                for word in words.split():
                    if word in characters:
                        continue
                    if word.lower() == wordcount:
                        word_cnt += 1

    if action == "delete":
        if file:
            Document.objects.all().last().delete()
        else:
            return render(request, "empty.html")

    return render(request, "upload.html", {"form": form, "word_cnt": word_cnt})
