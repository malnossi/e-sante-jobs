from rest_framework import serializers

from accounts.fields import CurrentUserStudentProfileDefault

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=CurrentUserStudentProfileDefault())

    class Meta:
        model = Post
        fields = '__all__'
