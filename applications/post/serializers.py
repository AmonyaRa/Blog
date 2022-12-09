from rest_framework import serializers

from applications.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source='owner.username')  # выводит owner (имя)б, если хотим через id, то вместо username можете написать id

    class Meta:
        model = Post
        fields = '__all__'
