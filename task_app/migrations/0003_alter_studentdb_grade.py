# Generated by Django 4.0.3 on 2022-03-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0002_alter_studentdb_grade_alter_studentdb_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdb',
            name='grade',
            field=models.CharField(default='grade', max_length=10),
        ),
    ]
