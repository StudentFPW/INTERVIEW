from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', )
    wordcount = models.CharField(max_length=10, )
