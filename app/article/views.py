import json
from pprint import pprint
# Django
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Django Rest
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import JSONParser


# Business logic imports
from .serializers import ArticleSerializer
from .models import *



@api_view(['POST'])
@permission_classes([AllowAny])
def ArticleCreateView(request, pk=None):
    context = {}
    get_author = None
    try:
        get_author = Author.objects.get(pk=pk)
    except:
        get_author = None

    if get_author:
        if request.method == 'POST':
            data = JSONParser().parse(request)
            article = None
            try:
                article = Article.objects.create(
                    author = get_author,
                    title = data.get('title'),
                    body = data.get('body'),
                    active = True
                )
            except:
                data = json.dumps({'message': 'Server Error', 'status': 500})
                return HttpResponse(data, content_type='application/json')

            serializer = ArticleSerializer(article, many=False)
            context['status'] = '200'
            context['data'] = serializer.data
            context['message'] = 'Succesfully Created Article'
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')
        else:
            data = json.dumps({'message': 'Access Denied', 'status': 401})
            return HttpResponse(data, content_type='application/json')
    else:
        to_send = json.dumps({'message': 'Author does not exist', 'status': 404})
        return HttpResponse(to_send, content_type='application/json')


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.filter(active = True)
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def ArticleDetailView(request, pk=None):
    context = {}
    article = None
    try:
        article = Article.objects.get(pk=pk)
    except:
        article = None

    if article:
        serializer = ArticleSerializer(article, many=False)
        if request.method == 'GET':
            context['status'] = '200'
            context['message'] = '{}'.format(str(article.title))
            context['data'] = serializer.data
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')
            
        elif request.method == 'DELETE':
            article.active = False
            article.save()

            context['status'] = '200'
            context['message'] = 'DELETED: {}'.format(article.title)
            context['data'] = serializer.data
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')

        elif request.method == 'PUT':
            data = JSONParser().parse(request)

            '''Update User'''
            article.title = data.get('title')
            article.body = data.get('body')
            article.save()
        
            context['status'] = '200'
            context['data'] = serializer.data
            context['message'] = 'Succesfully Updated Article'
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')
        else:
            data = json.dumps({'message': 'Access Denied', 'status': 401})
            return HttpResponse(data, content_type='application/json')
    else:
        to_send = json.dumps({'message': 'Article Not Found', 'status': 404})
        return HttpResponse(to_send, content_type='application/json')

