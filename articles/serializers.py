from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')
    class Meta:
        model = Article
        fields = ["title","content","user"]






