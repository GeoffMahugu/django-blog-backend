from rest_framework import serializers

from wayapay.account.models import Account


# class UserRegistrationSerializer(serializers.ModelSerializer):
#     url = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = UserRegistration
#         fields = [
#             'url',
#             'first_name',
#             'middle_name',
#             'last_name',
#             'email',
#             'phone_number',
#             'terms',
#             'timestamp',
#             'updated',
#         ]

#         read_only_fields = [
#             'pk',
#             'timestamp',
#             'updated',
#         ]

#     def get_url(self, obj):
#         request = self.context.get("request",)
#         return obj.get_api_url(request=request)


class AccountSerializer(serializers.ModelSerializer):  # forms.ModelForm
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Account
        fields = [
            'url',
            'slug',
            'pk',
            'user',
            'first_name',
            'middle_name',
            'last_name',
            'phone_number',
            'telephone',
            'email',
            'active',
            'token_access',
            'token_refresh',
            'timestamp',
            'updated',
        ]
        read_only_fields = [
            'url',
            'slug',
            'pk',
            'user',
            'token',
            'timestamp',
            'updated',
        ]

    # converts to JSON
    # validations for data passed

    def get_url(self, obj):
        # request
        request = self.context.get("request",)
        return obj.get_api_url(request=request)

    # def validate_title(self, value):
    #     qs = Account.objects.filter(title__iexact=value)  # including instance
    #     if self.instance:
    #         qs = qs.exclude(pk=self.instance.pk)
    #     if qs.exists():
    #         raise serializers.ValidationError(
    #             "This title has already been used")
    #     return value
