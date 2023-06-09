from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import *


def upload_file(request):
    wordcount = request.POST.get("wordcount")
    action = request.POST.get("action")
    word_cnt = 0
    file = Document.objects.all()

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if file:
                direct = Document.objects.filter(id=Document.objects.all().values().last()["id"]).values().last()["docfile"]
                with open(f"media/{direct}", encoding="utf-8") as file:
                    for word in file:
                        if word.replace("\n", "") == wordcount:
                            word_cnt += 1
    else:
        form = UploadFileForm()

    if action == "delete":
        if file:
            file.filter(id=Document.objects.all().values().last()["id"]).delete()
        else:
            return redirect("upload")

    return render(request, "upload.html", {"form": form, "word_cnt": word_cnt})
