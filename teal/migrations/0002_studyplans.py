# Generated by Django 3.1.7 on 2021-04-20 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyPlans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=128, verbose_name='Name')),
                ('version', models.IntegerField(default='1', verbose_name='Version')),
                ('credits', models.IntegerField()),
                ('courses', models.JSONField()),
                ('study_year_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teal.studyyear', verbose_name='study_year_id')),
            ],
        ),
    ]
