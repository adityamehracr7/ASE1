# Generated by Django 2.1.3 on 2018-11-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_dash', '0010_auto_20181118_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examtype',
            name='exam_type',
            field=models.CharField(choices=[('2', 'MID2'), ('5', 'END'), ('4', 'LAB'), ('3', 'PROJECT'), ('1', 'MID1')], default='2', max_length=20),
        ),
    ]