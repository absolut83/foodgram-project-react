from django.shortcuts import render
from rest_framework import filters, status, viewsets, mixins
from .serializers import (UserMeSerializer, UserSerializer)
from users.models import User
from rest_framework.pagination import PageNumberPagination
from .permissions import AdminPermission, AuthorOrReadonly, ReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from djoser.views import TokenCreateView
from .serializers import LoginSerializer
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #lookup_field = 'username'
    #pagination_class = PageNumberPagination
    #permission_classes = (AdminPermission,)
    #filter_backends = (filters.SearchFilter,)
    #search_fields = ('=username',)

class TokenCreateWithCheckBlockStatusView(TokenCreateView):
    def _action(self, serializer):
        return super()._action(serializer)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    #renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Обратите внимание, что мы не вызываем метод save() сериализатора, как
        # делали это для регистрации. Дело в том, что в данном случае нам
        # нечего сохранять. Вместо этого, метод validate() делает все нужное.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)