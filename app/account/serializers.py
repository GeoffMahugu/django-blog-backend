from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):  
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Author
        fields = [
            'url',
            'slug',
            'pk',
            'user',
            'first_name',
            'last_name',
            'email',
            'active',
            'timestamp',
            'updated',
        ]
        read_only_fields = [
            'url',
            'slug',
            'user',
            'pk',
            'author',
            'timestamp',
            'updated',
        ]

    def get_url(self, obj):
        # request
        request = self.context.get("request",)
        return obj.get_api_url(request=request)
