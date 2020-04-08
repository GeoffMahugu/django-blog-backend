import json
from pprint import pprint
# Django
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Django Rest
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import JSONParser


# Twillio Functions
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# JWT Auth
from rest_framework_simplejwt.tokens import RefreshToken

# Bcrypt
import bcrypt


# Business logic imports
from .serializers import AccountSerializer
from wayapay.account.models import *
from wayapay.settings.base import TWILLIO_ACCOUNT_SID, TWILLIO_TOKEN, TWILLIO_SENDER


def generate_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def GenerateVerificationCode():
    verification_code = get_random_string(length=6, allowed_chars='1234567890')
    return verification_code


def SendSMS(to, body):
    client = Client(TWILLIO_ACCOUNT_SID, TWILLIO_TOKEN)
    try:
        message = client.messages.create(
            to='+254{}'.format(to), from_=TWILLIO_SENDER, body=body)
    except TwilioRestException as e:
        print(e)


# @api_view(['GET', 'POST'])
# def SendSMSViewSet(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         to = '+254708808521'
#         to = '+254720777248'
#         verification_code = GenerateVerificationCode()
#         body = 'From Joppy: Your WayaPay Verification Code is: {}'.format(
#             verification_code)

#         SendSMS(to, body)
#         return Response({'message': 'Sent'})
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def UserRegistrationView(request, pk=None):
    context = {}
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print('REGISTER DATA://////////////////////////')
        pprint(data)

        '''Create User'''
        user = User.objects.get_or_create(
            username=data.get('national_id')
        )

        if user[1] == True:
            '''New User'''
            user[0].set_password('0000')
            user[0].first_name = data.get('first_name')
            user[0].last_name = data.get('last_name')
            user[0].email = '{}@google.com'.format(data.get('national_id'))
            user[0].save()

            get_token = generate_token(user[0])
            verification_code = GenerateVerificationCode()

            saved_token = None
            register_user = UserRegistration.objects.get_or_create(
                user=user[0]
            )

            try:
                register_user[0].token_access = str(get_token.get('access'))
                register_user[0].token_refresh = str(get_token.get('refresh'))
                register_user[0].verification_code = verification_code
                register_user[0].phone_number = data.get('phone_number')
                register_user[0].save()
            except:
                saved_token = None

            to = data.get('phone_number')
            body = 'Your WayaPay Verification Code is: {}'.format(
                verification_code)

            SendSMS(to, body)

            context['status'] = '200'
            context['message'] = 'Your Verification Code has been sent.'
            data['verification_code'] = verification_code
            context['data'] = data
            context['token'] = get_token
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')
        else:
            '''Existing User'''
            context['status'] = '403'
            context['message'] = 'User already exists'
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')

    else:
        context['status'] = '401'
        context['message'] = 'Access Denied'
        to_send = json.dumps(context)
        return HttpResponse(to_send, content_type='application/json')


@api_view(['POST'])
@permission_classes([AllowAny])
# @permission_classes([IsAuthenticated])
def UserLoginView(request, pk=None):
    context = {}
    if request.method == 'POST':
        data = JSONParser().parse(request)

        print('LOGIN DATA://////////////////////////')
        pprint(data)

        '''Get User'''
        user_account = None
        try:
            user_account = Account.objects.get(
                user__username__iexact=data.get('national_id'))
        except:
            context['status'] = '401'
            context['message'] = 'Access Denied: Account does not exist.'
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')

        if user_account:

            wallet_pin = None
            try:
                wallet_pin = WalletPin.objects.get(
                    account_holder=user_account
                )
            except:
                context['status'] = '401'
                context['message'] = 'Access Denied: Wallet Pin does not exist.'
                to_send = json.dumps(context)
                return HttpResponse(to_send, content_type='application/json')

            message = ''
            if wallet_pin != None:

                get_code = '{}'.format(data.get('pin')).encode()
                hashed = '{}'.format(wallet_pin.pin).encode()

                if bcrypt.checkpw(get_code, hashed):
                    message = 'Successfull verification'
                    context['status'] = '200'
                    context['message'] = message
                    context['data'] = data
                    serializer = AccountSerializer(user_account, many=False)

                    context['data']['profile'] = serializer.data
                    to_send = json.dumps(context)
                else:
                    message = 'Access Denied: Pin Does not Match'

                    context['status'] = '401'
                    context['message'] = message
                    context['data'] = data
                    to_send = json.dumps(context)

            return HttpResponse(to_send, content_type='application/json')
    else:
        context['status'] = '401'
        context['message'] = 'Access Denied'
        to_send = json.dumps(context)
        return HttpResponse(to_send, content_type='application/json')

# @api_view(['GET', 'POST'])
# def UserRegistrationDetailView(request, pk=None):
#     context = {}
#     register_user = None
#     try:
#         register_user = UserRegistration.objects.get(pk=pk)
#     except:
#         register_user = None

#     if register_user:

#         if request.method == 'GET':
#             serializer = UserRegistrationSerializer(register_user, many=False)

#             context['status'] = '200'
#             context['message'] = 'Found {}'.format(str(register_user))
#             context['data'] = serializer.data
#             to_send = json.dumps(context)
#             return HttpResponse(to_send, content_type='application/json')

#         elif request.method == 'POST':
#             data = JSONParser().parse(request)

#             '''Create User'''
#             # user = User.objects.get_or_create(
#             #     username=data.id_number
#             # )
#             pprint(user)

#             # pprint(data)

#             # serializer = ChatSerializer(data=data)
#             # if serializer.is_valid():
#             #     serializer.save()
#             #     return JsonResponse(serializer.data, status=201)
#             # return JsonResponse(serializer.errors, status=400)

#             context['status'] = '200'
#             context['message'] = 'Succesfully created user'
#             # context['data'] = serializer.data
#             to_send = json.dumps(data)
#             return HttpResponse(to_send, content_type='application/json')
#         else:
#             data = json.dumps({'message': 'Access Denied', 'status': 401})
#             return HttpResponse(data, content_type='application/json')
#     else:
#         to_send = json.dumps({'message': 'User Not Found', 'status': 404})
#         return HttpResponse(to_send, content_type='application/json')


@api_view(['POST'])
@permission_classes([AllowAny])
# @permission_classes([IsAuthenticated])
def UserVerificationView(request, pk=None):
    context = {}
    if request.method == 'POST':
        data = JSONParser().parse(request)

        print('VERIFICATION DATA://////////////////////////')
        pprint(data)

        '''Get User'''
        register_user = None
        try:
            register_user = UserRegistration.objects.get(
                user__username__iexact=data.get('national_id'))
        except:
            context['status'] = '401'
            context['message'] = 'Access Denied: Registration failed'
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')

        if register_user:
            if register_user.verification_code == data.get('verification_code'):
                account = Account.objects.get_or_create(
                    user=register_user.user
                )

                account[0].phone_number = register_user.phone_number
                account[0].token_access = register_user.token_access
                account[0].token_refresh = register_user.token_refresh
                account[0].term = True
                account[0].active = True
                account[0].save()

                to = account[0].phone_number
                body = 'Successfully verified your account.'
                # SendSMS(to, body)

                serializer = AccountSerializer(account[0], many=False)

                context['status'] = '200'
                context['message'] = body
                context['data'] = serializer.data
                to_send = json.dumps(context)
            else:
                context['status'] = '401'
                context['message'] = 'Verification code did not match'
                to_send = json.dumps(context)

            return HttpResponse(to_send, content_type='application/json')
    else:
        context['status'] = '401'
        context['message'] = 'Access Denied'
        to_send = json.dumps(context)
        return HttpResponse(to_send, content_type='application/json')


@api_view(['POST'])
@permission_classes([AllowAny])
# @permission_classes([IsAuthenticated])
def UserPinView(request, pk=None):
    context = {}
    if request.method == 'POST':
        data = JSONParser().parse(request)

        print('PIN DATA://////////////////////////')
        pprint(data)

        '''Get User'''
        user_account = None
        try:
            user_account = Account.objects.get(
                user__username__iexact=data.get('national_id'))
        except:
            context['status'] = '401'
            context['message'] = 'Access Denied: Account does not exist.'
            to_send = json.dumps(context)
            return HttpResponse(to_send, content_type='application/json')

        if user_account:
            wallet_pin = WalletPin.objects.get_or_create(
                account_holder=user_account
            )
            message = ''
            if wallet_pin[1] == True:
                message = 'Your wallet pin has been saved'
            else:
                message = 'Your wallet pin has been updated'

            get_code = '{}'.format(data.get('pin')).encode()
            hashed = bcrypt.hashpw(get_code, bcrypt.gensalt())
            wallet_pin[0].pin = hashed
            wallet_pin[0].save()

            # if bcrypt.checkpw(password, hashed):
            #     print("It Matches!")
            # else:
            #     print("It Does not Match :(")

            context['status'] = '200'
            context['message'] = message
            context['data'] = data
            to_send = json.dumps(context)

            return HttpResponse(to_send, content_type='application/json')
    else:
        context['status'] = '401'
        context['message'] = 'Access Denied'
        to_send = json.dumps(context)
        return HttpResponse(to_send, content_type='application/json')


class AccountAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# DetailView CreateView FormView
@permission_classes([IsAuthenticated])
class AccountRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def get_object(self):
        pk = self.kwargs.get("pk")
        return Account.objects.get(pk=pk)
