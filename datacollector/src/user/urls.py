
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TeacherViewSet, ProfileViewSet, UpdatePassword

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('changepass/', UpdatePassword.as_view(), name='change_password')
]

router = DefaultRouter()
router.register('', TeacherViewSet)
router.register('', ProfileViewSet)

urlpatterns += router.urls
