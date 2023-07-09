from rest_framework import serializers
from djagno_instar_clone.users.models import User
import models

class FeedAuthorSerializer(serializers.Moderlserializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "profile_photo",
        )

class CommentSerializer(serializers.Moderlserializer):
    author = FeedAuthorSerializer()
    class Meta:
        model = models.Comment
        fields = (
            "id",
            "contents",
            "author",
        )

class PostSerializer(serializers.Moderlserializer):
    comment_post = CommentSerializer(many=True)
    author = FeedAuthorSerializer()

    class Meta:
        model = models.Post
        fields = (
            "id",
            "image",
            "caption",
            "comment_post",
            "author",
            "image_likes",
        )