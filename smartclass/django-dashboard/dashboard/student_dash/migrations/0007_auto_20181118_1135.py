# Generated by Django 2.1.3 on 2018-11-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_dash', '0006_auto_20181118_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examtype',
            name='exam_type',
            field=models.CharField(choices=[('4', 'LAB'), ('3', 'PROJECT'), ('2', 'MID2'), ('1', 'MID1'), ('5', 'END')], default=2, max_length=20),
        ),
    ]
