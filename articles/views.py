from django.shortcuts import get_object_or_404
from .models import Article
from rest_framework import viewsets,generics
from rest_framework.response import Response
from .serializers import ArticleSerializer
from rest_framework.permissions import AllowAny
from .helpers import IsOwner,IsOwnerOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import status
from rest_framework.decorators import api_view
from rest_framework.authentication import authenticate
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#test
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

#viewset사용 
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [IsOwnerOrReadOnly]  #읽기전용 커스텀 
    def perform_create(self, serializer):
        print(self.request)
        serializer.save(user = self.request.user)

@api_view(["POST"])
def create_article(request):
   serializer=ArticleSerializer(data=request.data)
   if serializer.is_valid():
    print(request.user)
    serializer.save(user=request.user)   
    return Response(status=status.HTTP_201_CREATED)
   return Response(status=status.HTTP_400_BAD_REQUEST)

