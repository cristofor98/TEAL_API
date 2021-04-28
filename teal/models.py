from django.db import models

# Create your models here.



class StudyYear(models.Model):
  year = models.IntegerField(verbose_name='study_year', db_index=True, unique=True)     


class StudyPlans(models.Model):
  name = models.CharField(verbose_name='Name', db_index=True, max_length=128)
  study_year_id = models.ForeignKey(StudyYear, verbose_name='study_year_id', on_delete=models.CASCADE)
  version = models.IntegerField(verbose_name='Version', default='1')
  credits = models.IntegerField()
  courses = models.JSONField()

class Groups(models.Model):
  name = models.CharField(verbose_name='Name', db_index=True, max_length=128)
  start_year = models.IntegerField(verbose_name='start_year')
  number_of_students = models.IntegerField(verbose_name='number_of_students')
  LANGUAGE_TYPE = ((1,'Română'),
  	(2, 'Rusă'),
  	(3, 'Engleză'),
  	(4,'Franceză'),
  	)
  language = models.IntegerField(verbose_name='language', choices=LANGUAGE_TYPE)
  id_study_plan = models.ForeignKey(StudyPlans, verbose_name='id_study_plan', on_delete=models.CASCADE)
  FORMOFSTUDY_TYPE =((1, "la zi"), (2, "la frecvență"))
  form_of_study = models.IntegerField(verbose_name='language', choices=FORMOFSTUDY_TYPE)
  study_year_id = models.ForeignKey(StudyYear, verbose_name='study_year_id', on_delete=models.CASCADE)
  fantom = models.JSONField()

class Groupings(models.Model):
  faculty = models.CharField(verbose_name='faculty', db_index=True, max_length=128)
  study_year_id = models.ForeignKey(StudyYear, verbose_name='study_year_id', on_delete=models.CASCADE)
  FORMOFSTUDY_TYPE =((1, "la zi"), (2, "la frecvență"))
  form_of_study = models.IntegerField(verbose_name='language', choices=FORMOFSTUDY_TYPE)
  STATUS_TYPE = ((1,"Nu este verificat"), (2, "Verificat"))
  status =  models.IntegerField(verbose_name='language', choices=STATUS_TYPE)
  groupings = models.JSONField()