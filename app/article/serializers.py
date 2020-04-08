from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):  
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = [
            'url',
            'pk',
            'author',
            'title',
            'body',
            'timestamp',
            'updated',
        ]
        read_only_fields = [
            'url',
            'slug',
            'pk',
            'author',
            'timestamp',
            'updated',
        ]

    def get_url(self, obj):
        # request
        request = self.context.get("request",)
        return obj.get_api_url(request=request)
