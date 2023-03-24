from .models import *
from rest_framework import serializers
from rest_framework.serializers import IntegerField


class QuestionsSerializer(serializers.ModelSerializer):
    id = IntegerField(required=False)
    has_upvoted = serializers.SerializerMethodField('check_upvoted')
    has_bookmarked = serializers.SerializerMethodField('check_bookmarked')
    has_flagged = serializers.SerializerMethodField('check_flagged')

    def check_upvoted(self, Questions):
        
        instance = upvote_check.objects.filter(user_id=self.context.get("uID"))
        if instance.exists():
            if Questions.id in instance[0].question_id:
                flag=True
            else:
                flag=False
        else:
            flag = False
        return flag


    def check_bookmarked(self, Questions):
        
        instance = bookmarks.objects.filter(user_id=self.context.get("uID"))
        if instance.exists():
            if Questions.id in instance[0].question_id:
                flag=True
            else:
                flag=False
        else:
            flag = False
        return flag
    
    
    def check_flagged(self, Questions):
        
        instance = flag_check.objects.filter(user_id=self.context.get("uID"))
        if instance.exists():
            if Questions.id in instance[0].question_id:
                flag=True
            else:
                flag=False
        else:
            flag = False
        return flag
    
    

    class Meta:
        model = Questions
        fields = ['id','type','question','q_image','q_file','answer','BT_level','max_marks','option_1','option_2','option_3','option_4','correct_option','has_upvoted','has_bookmarked','has_flagged']
        # fields = '__all__'  # upvotes/flag count disabled

class TopicsSerializer(serializers.ModelSerializer):
    id = IntegerField(required=False)
    questions = QuestionsSerializer(many=True,required=False)

    class Meta:
        model = Topics
        fields = ['id','name', 'questions']
        # fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    id = IntegerField(required=False)
    topics = TopicsSerializer(many=True,required=False)

    class Meta:
        model = Module
        fields = ['id','name', 'topics']
        # fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    id = IntegerField(required=False)
    modules = ModuleSerializer(many=True,required=False)

    def create(self, validated_data):
        modules = validated_data.pop("modules")

        course = Courses(**validated_data)
        course.save()

        for obj in modules:
            addr_obj = Module(**obj)
            addr_obj.save()
            course.modules.add(addr_obj)

        return course
    
    # def update(self, course, validated_data):
    #     modules = validated_data.pop("modules", [])

    #     for obj in modules:
    #         print(obj)
    #         print(course)
    #         # try:
    #         #     item = courseobj.id
    #         # course
    #         # Module.objects.filter(id=obj.id).update
    #     # for loop on (id req=fals para)
    #     # industry_data = validated_data.pop('Industry')
    #     # id = course.modules.id 
    #     # Industry.objects.filter(id=id).update(**industry_data)

    #     # for item in validated_data:
    #     #     if Vendor._meta.get_field(item):
    #     #         setattr(vendor, item, validated_data[item])
        
    #     # course.save()

    #     return Courses.objects.get(id=course.id)

    class Meta:
        model = Courses
        fields = ['id','name', 'code','modules']
        # fields = '__all__'
        

class MCQSerializer(serializers.ModelSerializer):
    id = IntegerField(required=False)
    
    class Meta:
        model = MCQ
        fields = '__all__'