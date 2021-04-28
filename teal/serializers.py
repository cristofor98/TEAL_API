from rest_framework import serializers
from . models import StudyYear, StudyPlans, Groups, Groupings

class StudyYearSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudyYear
		fields = '__all__'
			


class StudyPlansSerializer(serializers.ModelSerializer):
    class Meta:
    	model = StudyPlans
    	fields = '__all__'


class GroupsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Groups
		fields = '__all__'
			
class GroupingsSerializar(serializers.ModelSerializer):
	class Meta:
		model = Groupings
		fields = '__all__'
			