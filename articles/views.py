from .models import Article
from rest_framework import viewsets,generics
from rest_framework.response import Response
from .serializers import ArticleSerializer
from rest_framework.permissions import AllowAny
from .helpers import IsOwner,IsOwnerOrReadOnly

from rest_framework.views import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
# Create your views here.



User = get_user_model()

#viewset사용 
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [IsOwnerOrReadOnly] 
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



