from django.shortcuts import get_object_or_404
from .models import Article
from rest_framework import viewsets,generics
from rest_framework.response import Response
from .serializers import ArticleSerializer

# Create your views here.


#viewset사용 
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

#