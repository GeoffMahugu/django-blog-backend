



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
from .serializers import AuthorSerializer
from .models import *


@api_view(['POST'])
@permission_classes([AllowAny])
def AuthorSignupView(request):
    context = {}

    if request.method == 'POST':
        data = JSONParser().parse(request)

        '''Create User'''
        user = User.objects.get_or_create(
            email=data.get('email')
        )
        if user[1] == True:
            '''Update User'''
            user[0].first_name = data.get('first_name')
            user[0].last_name = data.get('last_name')
            user[0].save()

            author = Author.objects.get_or_create(
                user = user[0] 
            ) 
            author[0].active = data.get('active')
            author[0].save()

            serializer = AuthorSerializer(author[0], many=False)

            context['status'] = '200'
            context['data'] = serializer.data
            context['message'] = 'Succesfully Created Author'
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')
        else:
            '''Existing User'''
            context['status'] = '403'
            context['message'] = 'Author already exists'
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')
    else:
        data = json.dumps({'message': 'Access Denied', 'status': 401})
        return HttpResponse(data, content_type='application/json')


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.filter(active = True)
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def AuthorDetailView(request, pk=None):
    context = {}
    get_author = None
    try:
        get_author = Author.objects.get(pk=pk)
    except:
        get_author = None

    if get_author:
        serializer = AuthorSerializer(get_author, many=False)
        if request.method == 'GET':
            context['status'] = '200'
            context['message'] = 'Found {}'.format(str(get_author))
            context['data'] = serializer.data
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')
            
        elif request.method == 'DELETE':
            get_author.active = False
            get_author.save()

            context['status'] = '200'
            context['message'] = 'DELETED {}'.format(str(get_author))
            context['data'] = serializer.data
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')

        elif request.method == 'PUT':
            data = JSONParser().parse(request)

            '''Update User'''
            get_author.user.first_name = data.get('first_name')
            get_author.user.last_name = data.get('last_name')
            get_author.user.email = data.get('email')
            get_author.user.save()

            get_author.active = data.get('active')
            get_author.save()
        
            context['status'] = '200'
            context['data'] = serializer.data
            context['message'] = 'Succesfully Updated Author'
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')
        else:
            data = json.dumps({'message': 'Access Denied', 'status': 401})
            return HttpResponse(data, content_type='application/json')
    else:
        to_send = json.dumps({'message': 'Author Not Found', 'status': 404})
        return HttpResponse(to_send, content_type='application/json')
