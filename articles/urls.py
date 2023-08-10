from django.urls import path,include
from rest_framework import routers
from . import views



app_name = "articles"

router = routers.DefaultRouter()
router.register("", views.ArticleViewSet, basename="articles")


urlpatterns = [
    path("", include(router.urls)),
    path("list/", views.ArticleViewSet.as_view({"post": 'create','get': "list"})),

]