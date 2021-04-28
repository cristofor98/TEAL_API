from django.urls import path
from . views import StudyYearsView, StudyYearDetailView, StudyPlansView, StudyPlanDetailView, GroupsView, GroupDetailView, GroupingsView, GroupingDetailView

urlpatterns = [
    path('studyyear/', StudyYearsView.as_view(), name='StudyYearView'),
    path('studyyear/<int:pk>/', StudyYearDetailView.as_view(), name='StudyYearDetailView'),
    path('studyplans/', StudyPlansView.as_view(), name='StudyPlansView'),
    path('studyplans/<int:pk>/', StudyPlanDetailView.as_view(), name='StudyPlanDetailView'),
    path('groups/', GroupsView.as_view(), name='GroupsView'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='GroupDetailView'),
    path('groupings/', GroupingsView.as_view(), name='GroupingsView'),
    path('groupings/<int:pk>/', GroupingDetailView.as_view(), name='GroupingDetailView'),
] 