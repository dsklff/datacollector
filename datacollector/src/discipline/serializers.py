from rest_framework import serializers
from .models import *


class LaboratoryWorkSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        return 'http://localhost:8000' + obj.file.url


    class Meta:
        model = LaboratoryWork
        fields = ('id', 'name', 'desc', 'file', 'file_url', 'teacher', 'discipline')


class QuizSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        return 'http://localhost:8000' + obj.file.url


    class Meta:
        model = Quiz
        fields = ('id', 'name', 'desc', 'file', 'file_url', 'teacher', 'discipline')


class SISSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        return 'http://localhost:8000' + obj.file.url


    class Meta:
        model = SIS
        fields = ('id', 'name', 'desc', 'file', 'file_url', 'teacher', 'discipline')


class TSISSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        return 'http://localhost:8000' + obj.file.url


    class Meta:
        model = TSIS
        fields = ('id', 'name', 'desc', 'file', 'file_url', 'teacher', 'discipline')


class FinalSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        return 'http://localhost:8000' + obj.file.url


    class Meta:
        model = Final
        fields = ('id', 'name', 'desc', 'file', 'file_url', 'teacher', 'discipline')


class SyllabusSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        return 'http://localhost:8000' + obj.file.url


    class Meta:
        model = Syllabus
        fields = ('id', 'name', 'desc', 'file', 'file_url', 'teacher', 'discipline')


class MidtermSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        return 'http://localhost:8000' + obj.file.url


    class Meta:
        model = Midterm
        fields = ('id', 'name', 'desc', 'file', 'file_url', 'teacher', 'discipline')


class EndtermSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        return 'http://localhost:8000' + obj.file.url


    class Meta:
        model = Endterm
        fields = ('id', 'name', 'desc', 'file', 'file_url', 'teacher', 'discipline')


class LectureSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        return 'http://localhost:8000' + obj.file.url


    class Meta:
        model = Lecture
        fields = ('id', 'name', 'desc', 'file', 'file_url', 'teacher', 'discipline')


class DisciplineSerializer(serializers.ModelSerializer):
    labworks = LaboratoryWorkSerializer(many=True)
    quizes = QuizSerializer(many=True)
    sises = SISSerializer(many=True)
    tsises = TSISSerializer(many=True)
    finals = FinalSerializer(many=True)
    syllabuses = SyllabusSerializer(many=True)
    midterms = MidtermSerializer(many=True)
    endterms = EndtermSerializer(many=True)
    lectures = LectureSerializer(many=True)

    class Meta:
        model = Discipline
        fields = ('id', 'name', 'credit_amount', 'desc', 'teacher', 'labworks', 'quizes', 'sises', 'tsises',
                  'finals', 'syllabuses', 'midterms', 'endterms', 'lectures')


class DisciplineCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discipline
        fields = '__all__'
