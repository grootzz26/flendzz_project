# Generated by Django 4.0.3 on 2022-03-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0007_alter_studentdb_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdb',
            name='marks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
