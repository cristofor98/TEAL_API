from rest_framework.response import Response
from rest_framework import generics
from . models import StudyYear, StudyPlans, Groups, Groupings
from . serializers import StudyYearSerializer, StudyPlansSerializer, GroupsSerializer, GroupingsSerializar

# Create your views here.
# RetrieveAPIView - used for read-only endpoints to represent
class StudyYearsView(generics.ListCreateAPIView):
	queryset = StudyYear.objects.all()
	serializer_class = StudyYearSerializer
#	def get(self, request, *args, **kwargs):
#		queryset = self.get_queryset()
#		serializer = StudyYearSerializer(queryset, many=True)
#		return Response(serializer.data)


class StudyYearDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudyYearSerializer
    queryset = StudyYear.objects.all()

class StudyPlansView(generics.ListCreateAPIView):
    serializer_class = StudyPlansSerializer
    queryset = StudyPlans.objects.all()

class StudyPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = StudyPlansSerializer
	queryset = StudyPlans.objects.all()

class GroupsView(generics.ListCreateAPIView):
	serializer_class = GroupsSerializer
	queryset = Groups.objects.all()

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = GroupsSerializer
	queryset = Groups.objects.all()

class GroupingsView(generics.ListCreateAPIView):
	serializer_class = GroupingsSerializar
	queryset = Groupings.objects.all()

class GroupingDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = GroupingsSerializar
	queryset = Groupings.objects.all()
