# Generated by Django 3.0.3 on 2020-04-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=100)),
                ('employee_name', models.CharField(max_length=100)),
                ('training_name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('date_of_completion', models.CharField(max_length=100)),
                ('total_training_hours', models.CharField(max_length=100)),
                ('hours_spent_today', models.CharField(max_length=100)),
                ('training_type', models.CharField(max_length=100)),
                ('skill', models.CharField(max_length=100)),
                ('certification_availability', models.CharField(max_length=100)),
                ('certified', models.CharField(max_length=100)),
                ('lex_link', models.CharField(max_length=100)),
                ('task', models.CharField(max_length=100)),
                ('task_description', models.CharField(max_length=100)),
                ('total_hours', models.CharField(max_length=100)),
                ('assessment_availability', models.CharField(max_length=100)),
                ('assessment_completion', models.CharField(max_length=100)),
            ],
        ),
    ]
