# Generated by Django 2.1.3 on 2018-11-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_dash', '0019_auto_20181118_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examtype',
            name='exam_type',
            field=models.CharField(choices=[('mid1', 'MID1'), ('lab', 'LAB'), ('end', 'END'), ('mid2', 'MID2'), ('project', 'PROJECT')], default='mid1', max_length=20),
        ),
    ]