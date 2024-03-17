from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', views.ArticleViewSet, basename='article_viewset')

urlpatterns = [
    path('home/', views.articles, name='articles'),
    path('article_details/<int:pk>', views.article_details, name='article_details'),

    path('articles/', views.ArticlesAPIView.as_view(), name='class_articles'),
    path('details/<int:pk>', views.ArticleDetailsAPIView.as_view(), name='class_details'),

    path('generics/', views.GenericAPIView.as_view(), name='generic_articles'),

    path('', include(router.urls)),
]