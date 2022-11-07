from django.shortcuts import render
from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import *
from ..publications.serializers import AttachmentSerializer
from .models import *


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineCreateSerializer
    permission_classes =  (IsAuthenticated, )
    parser_classes = [MultiPartParser, JSONParser]

    def perform_create(self, serializer):
        return serializer.save(teacher=self.request.user)

    def get_queryset(self):
        queryset = Discipline.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.kwargs['pk'])
        return obj

    def list(self, request, *args, **kwargs):
        disciplines = Discipline.objects.filter(teacher=self.request.user)
        serializer = DisciplineCreateSerializer(disciplines, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        discipline = Discipline.objects.get(id=pk)
        if discipline not in Discipline.objects.filter(teacher=self.request.user):
            return Response('No data')
        serializer = DisciplineSerializer(discipline)
        print(request.get_host())
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = DisciplineCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(teacher=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=[IsAuthenticated])
    def labworks(self, request, pk):
        if request.method == 'GET':
            discipline = get_object_or_404(Discipline, id=pk)
            labworks = LaboratoryWork.objects.filter(discipline_id=discipline.id)
            serializer = LaboratoryWorkSerializer(labworks, many=True, context={'request': request})

            return Response(serializer.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = LaboratoryWorkSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(teacher=self.request.user, discipline=instance)
                return Response(serializer.data)
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=[IsAuthenticated])
    def quizes(self, request, pk):
        if request.method == 'GET':
            discipline = get_object_or_404(Discipline, id=pk)
            quizes = Quiz.objects.filter(discipline_id=discipline.id)
            serializer = QuizSerializer(quizes, many=True, context={'request': request})

            return Response(serializer.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = QuizSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(teacher=self.request.user, discipline=instance)
                return Response(serializer.data)
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=[IsAuthenticated])
    def midterms(self, request, pk):
        if request.method == 'GET':
            discipline = get_object_or_404(Discipline, id=pk)
            midterms = Midterm.objects.filter(discipline_id=discipline.id)
            serializer = MidtermSerializer(midterms, many=True, context={'request': request})

            return Response(serializer.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = MidtermSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(teacher=self.request.user, discipline=instance)
                return Response(serializer.data)
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=[IsAuthenticated])
    def endterms(self, request, pk):
        if request.method == 'GET':
            discipline = get_object_or_404(Discipline, id=pk)
            endterms = Endterm.objects.filter(discipline_id=discipline.id)
            serializer = EndtermSerializer(endterms, many=True, context={'request': request})

            return Response(serializer.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = EndtermSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(teacher=self.request.user, discipline=instance)
                return Response(serializer.data)
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=[IsAuthenticated])
    def lectures(self, request, pk):
        if request.method == 'GET':
            discipline = get_object_or_404(Discipline, id=pk)
            lectures = Lecture.objects.filter(discipline_id=discipline.id)
            serializer = LectureSerializer(lectures, many=True, context={'request': request})

            return Response(serializer.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = LectureSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(teacher=self.request.user, discipline=instance)
                return Response(serializer.data)
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=[IsAuthenticated])
    def sises(self, request, pk):
        if request.method == 'GET':
            discipline = get_object_or_404(Discipline, id=pk)
            sises = SIS.objects.filter(discipline_id=discipline.id)
            serializer = SISSerializer(sises, many=True, context={'request': request})

            return Response(serializer.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = SISSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(teacher=self.request.user, discipline=instance)
                return Response(serializer.data)
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=[IsAuthenticated])
    def tsises(self, request, pk):
        if request.method == 'GET':
            discipline = get_object_or_404(Discipline, id=pk)
            tsises = TSIS.objects.filter(discipline_id=discipline.id)
            serializer = TSISSerializer(tsises, many=True, context={'request': request})

            return Response(serializer.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = TSISSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(teacher=self.request.user, discipline=instance)
                return Response(serializer.data)
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=[IsAuthenticated])
    def syllabuses(self, request, pk):
        if request.method == 'GET':
            discipline = get_object_or_404(Discipline, id=pk)
            syllabuses = Syllabus.objects.filter(discipline_id=discipline.id)
            serializer = SyllabusSerializer(syllabuses, many=True, context={'request': request})

            return Response(serializer.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = SyllabusSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(teacher=self.request.user, discipline=instance)
                return Response(serializer.data)
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True, permission_classes=[IsAuthenticated])
    def finals(self, request, pk):
        if request.method == 'GET':
            discipline = get_object_or_404(Discipline, id=pk)
            finals = Final.objects.filter(discipline_id=discipline.id)
            serializer = FinalSerializer(finals, many=True, context={'request': request})

            return Response(serializer.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = FinalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(teacher=self.request.user, discipline=instance)
                return Response(serializer.data)
            return Response(serializer.errors)


class LaboratoryWorkViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = LaboratoryWork.objects.all()
    serializer_class = LaboratoryWorkSerializer
    permission_classes = (IsAuthenticated, )


class QuizViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsAuthenticated, )


class LectureViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated, )


class SISViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = SIS.objects.all()
    serializer_class = SISSerializer
    permission_classes = (IsAuthenticated, )


class TSISViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = TSIS.objects.all()
    serializer_class = TSISSerializer
    permission_classes = (IsAuthenticated, )


class MidtermViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Midterm.objects.all()
    serializer_class = MidtermSerializer
    permission_classes = (IsAuthenticated, )


class EndtermViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Endterm.objects.all()
    serializer_class = EndtermSerializer
    permission_classes = (IsAuthenticated, )


class SyllabusViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer
    permission_classes = (IsAuthenticated, )


class FinalViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Final.objects.all()
    serializer_class = FinalSerializer
    permission_classes = (IsAuthenticated, )
