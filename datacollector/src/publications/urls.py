from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [

]

router = DefaultRouter()
router.register('', PublicationCustomViewSet)
router.register('attachment', AttachmentViewSet)
router.register('journal', JournalViewSet)
urlpatterns += router.urls
