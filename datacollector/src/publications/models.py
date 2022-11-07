from django.db import models

# Create your models here.
from src.user.models import Teacher


class Publication(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True, null=True, default='')
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Attachment(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='attachments/')
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='attachments')

    def __str__(self):
        return self.name


class Journal(models.Model):
    name = models.CharField(max_length=200)
    issn = models.CharField(max_length=9)
    issue = models.CharField(max_length=100)
    date_of_issue = models.DateField(null=True, blank=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='journals')

    def __str__(self):
        return self.name

