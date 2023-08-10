from django.shortcuts import get_object_or_404
from .models import Article
from rest_framework import viewsets,generics
from rest_framework.response import Response
from .serializers import ArticleSerializer
from rest_framework.permissions import AllowAny
from .permission import IsOwner,IsOwnerOrReadOnly
# Create your views here.


#viewset사용 
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [IsOwnerOrReadOnly]  #읽기전용 커스텀 

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

