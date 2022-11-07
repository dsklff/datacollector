from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [

]

router = DefaultRouter()
router.register('', DisciplineViewSet)
router.register('labwork', LaboratoryWorkViewSet)
router.register('quiz', QuizViewSet)
router.register('midterm', MidtermViewSet)
router.register('endterm', EndtermViewSet)
router.register('sis', SISViewSet)
router.register('tsis', TSISViewSet)
router.register('lecture', LectureViewSet)
router.register('syllabus', SyllabusViewSet)
router.register('final', FinalViewSet)
urlpatterns += router.urls
