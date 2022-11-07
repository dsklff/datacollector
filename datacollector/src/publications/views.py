from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import *
from .serializers import *


# class PublicationViewSet(viewsets.ModelViewSet):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationSerializer
#     permission_classes = (IsAuthenticated, )
#
#     def perform_create(self, serializer):
#         return serializer.save(author=self.request.user)
#
#     @action(methods=['GET'], detail=False)
#     def my(self, serializer):
#         publications = Publication.objects.filter(author=self.request.user)
#         serializer = self.get_serializer(publications, many=True)
#         return Response(serializer.data)


class PublicationCustomViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationCustomSerializer
    permission_classes = (IsAuthenticated, )
    parser_classes = (MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Publication.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.kwargs['pk'])
        return obj

    def list(self, request, *args, **kwargs):
        publications = Publication.objects.filter(author=self.request.user)
        serializer = PublicationCustomSerializer(publications, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        publication = Publication.objects.get(id=pk)
        if publication not in Publication.objects.filter(author=self.request.user):
            return Response('No data')
        serializer = PublicationSerializer(publication)
        print(request.get_host())
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PublicationCustomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=[IsAuthenticated])
    def attachments(self, request, pk):
        if request.method == 'GET':
            publication = get_object_or_404(Publication, id=pk)
            attachments = Attachment.objects.filter(publication_id=publication.id)
            serializer = AttachmentSerializer(attachments, many=True, context={'request': request})

            return Response(serializer.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = AttachmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(publication=instance)
                return Response(serializer.data)
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=[IsAuthenticated])
    def journals(self, request, pk):
        if request.method == 'GET':
            publication = get_object_or_404(Publication, id=pk)
            journals = Journal.objects.filter(publication_id=publication.id)
            serializer = JournalSerializer(journals, many=True)

            return Response(serializer.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = JournalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(publication=instance)
                return Response(serializer.data)
            return Response(serializer.errors)


class AttachmentViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = (IsAuthenticated, )


class JournalViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = (IsAuthenticated, )
