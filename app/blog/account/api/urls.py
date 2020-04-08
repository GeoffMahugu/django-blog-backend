from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


from .views import AccountRudView, AccountAPIView, UserRegistrationView, UserVerificationView, UserPinView, UserLoginView

urlpatterns = [
    url(r'profile/$', AccountAPIView.as_view(), name='account-listcreate'),
    url(r'^profile/(?P<pk>\d+)/$', AccountRudView.as_view(), name='account-rud'),


    url(r'^user-registration/$', UserRegistrationView,
        name='account-user-registration'),
    url(r'^user-verification/$', UserVerificationView,
        name='account-user-verification'),
    url(r'^user-pin/$', UserPinView,
        name='account-user-pin'),
    url(r'^user-login/$', UserLoginView,
        name='account-user-login'),


    # url(r'^user-registration/(?P<pk>\d+)/$', UserRegistrationDetailView,
    #     name='account-user-registration-details')
]
