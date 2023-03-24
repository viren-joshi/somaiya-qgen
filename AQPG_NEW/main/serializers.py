from .models import *
from rest_framework import serializers
from rest_framework.serializers import IntegerField

class CoursesSerializer(serializers.ModelSerializer):
    id = IntegerField(required=False)
    
    class Meta:
        model = Courses
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    id = IntegerField(required=False)
    
    class Meta:
        model = Module
        fields = ['id','name']

class PostSerializer(serializers.ModelSerializer):
    id = IntegerField(required=False)
    upvoted = serializers.SerializerMethodField('check_upvoted')
    bookmarked = serializers.SerializerMethodField('check_bookmarked')
    flagged = serializers.SerializerMethodField('check_flagged')
    upvote_count = serializers.SerializerMethodField('upvote')
    flag_count = serializers.SerializerMethodField('flag')
    # print('l')

    def check_upvoted(self, Post):
        flag = False
        user = self.context.get("user")
        if Upvotes.objects.filter(user=user,post=Post).exists():
            flag =True
        return flag

    def check_bookmarked(self, Post):
        flag = False
        user = self.context.get("user")
        # print(user)
        # print(Bookmark.objects.filter(user=user,post=Post))
        if Bookmark.objects.filter(user=user,post=Post).exists():
            flag =True
        return flag

    def check_flagged(self, Post):
        flag = False
        user = self.context.get("user")
        if Flag.objects.filter(user=user,post=Post).exists():
            flag =True
        return flag

    def upvote(self, Post):
        flag = Upvotes.objects.filter(post=Post).count()
        return flag

    def flag(self, Post):
        flag = Flag.objects.filter(post=Post).count()
        return flag
    
    class Meta:
        model = Post
        fields = '__all__'

class BookmarkSerializer(serializers.ModelSerializer):
    id = IntegerField(required=False)
    post = PostSerializer(many=False)
    
    class Meta:
        model = Bookmark
        fields = '__all__'