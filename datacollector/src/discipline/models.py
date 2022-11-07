from django.db import models
from src.user.models import *
from src.publications.models import *


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    credit_amount = models.CharField(max_length=1, default=3)
    desc = models.CharField(max_length=500)
    teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LaboratoryWork(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    file = models.FileField(upload_to='edu_files/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='labworks', null=True, blank=True)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    file = models.FileField(upload_to='edu_files/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='quizes', null=True, blank=True)

    def __str__(self):
        return self.name


class Midterm(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    file = models.FileField(upload_to='edu_files/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='midterms', null=True, blank=True)

    def __str__(self):
        return self.name


class Endterm(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    file = models.FileField(upload_to='edu_files/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='endterms', null=True, blank=True)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    file = models.FileField(upload_to='edu_files/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='lectures', null=True, blank=True)

    def __str__(self):
        return self.name


class SIS(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    file = models.FileField(upload_to='edu_files/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='sises', null=True, blank=True)

    def __str__(self):
        return self.name


class TSIS(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    file = models.FileField(upload_to='edu_files/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='tsises', null=True, blank=True)

    def __str__(self):
        return self.name


class Syllabus(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    file = models.FileField(upload_to='edu_files/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='syllabuses', null=True, blank=True)

    def __str__(self):
        return self.name


class Final(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    file = models.FileField(upload_to='edu_files/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='finals', null=True, blank=True)

    def __str__(self):
        return self.name




# class TeacherFile(models.Model):
#
#     TYPES = [
#         ('Laboratory work', 'Laboratory work'),
#         ('Quiz', 'Quiz'),
#         ('Midterm', 'Midterm'),
#         ('Endterm', 'Endterm'),
#         ('Lecture', 'Lecture'),
#         ('SIS', 'SIS'),
#         ('TSIS', 'TSIS'),
#         ('Final', 'Final')
#     ]
#
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     type = models.CharField(max_length=100, choices=TYPES)
#     file = models.FileField(upload_to='files/teacher_files')
#
#
# # links model
#
# class Syllabus(models.Model):
#     discipline = models.ForeignKey(Discipline, on_delete=models.SET_NULL)
#     term = models.CharField(max_length=50)
#     duration = models.CharField(max_length=100)
#     prerequisites = models.CharField(max_length=200)
#     objectives = models.TextField(max_length=1000)
#     outcomes = models.TextField(max_length=1000)
#     literature = models.TextField(max_length=1000)
#
#
# class SyllabusWeeks(models.Model):
#     syllabus = models.ForeignKey(Syllabus, on_delete=models.SET_NULL)
#
#
#

