from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LoginAPIView, UserViewSet, TokenCreateWithCheckBlockStatusView


router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    #path('auth/', include('djoser.urls.authtoken')),
    path('auth/token/login/', LoginAPIView.as_view()),
    path('', include(router.urls)),
]