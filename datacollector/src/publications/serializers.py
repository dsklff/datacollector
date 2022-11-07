from rest_framework import serializers
from .models import *


class AttachmentSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        return 'http://localhost:8000' + obj.file.url

    class Meta:
        model = Attachment
        fields = ('id', 'name', 'file', 'file_url')

    # def to_internal_value(self, data):
    #     validated = {
    #         'id': data.get('id'),
    #         'name': data.get('name'),
    #         'file': 'localhost:8000' + data.get('file')
    #     }


class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = ('id', 'name', 'issue', 'date_of_issue', 'issn')


class PublicationSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True)
    journals = JournalSerializer(many=True)

    class Meta:
        model = Publication
        fields = ['id', 'name', 'description', 'author', 'attachments', 'journals']


class PublicationCustomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'

# class PublicationCreateSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Publication
#         fields = ['id', 'name',]
