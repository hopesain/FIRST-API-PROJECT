from . models import Article
from . serializers import ArticleSerializer
from rest_framework import status
from rest_framework.response import Response

#####################################################################################################
#FUNCTIONAL BASED VIEWS
from rest_framework.decorators import api_view
@api_view(['GET', 'POST'])
def articles(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('?')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])    
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##########################################################################################
#INTRODUCTION TO CLASS BASED VIEWS
from rest_framework.views import APIView
from django.http import Http404
class ArticlesAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all().order_by('?')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#############################################################################################
#INTRODUCTION TO MIXINS AND GENERIC CLASS BASED VIEWS
from rest_framework import mixins, generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by('?')
    authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
##################################################################################################################
#VIEWSETS AND ROUTERS
from rest_framework import viewsets
class ArticleViewSet(
    viewsets.GenericViewSet, mixins.CreateModelMixin,
    mixins.ListModelMixin, mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by('?')
######################################################################################################