from django.urls import path,include
from rest_framework import routers
from . import views





router = routers.DefaultRouter()
router.register("", views.ArticleViewSet)


urlpatterns = [
    path("",views.ArticleViewSet.as_view({"get": "list"}),name='list'),
    path("create/",views.ArticleViewSet.as_view({"post": "create"}),name='create'),
    path("detail/<int:pk>/",views.ArticleViewSet.as_view({"get": "retrieve"}),name='detail'),
    path("update/<int:pk>/",views.ArticleViewSet.as_view({"put": "update"}),name='update'),
    path("delete/<int:pk>/",views.ArticleViewSet.as_view({"delete": "destroy"}),name='delete'),

]