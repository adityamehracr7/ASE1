# Generated by Django 2.1.3 on 2018-11-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_dash', '0015_auto_20181118_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examtype',
            name='exam_type',
            field=models.CharField(choices=[('lab', 'LAB'), ('mid1', 'MID1'), ('project', 'PROJECT'), ('end', 'END'), ('mid2', 'MID2')], default='2', max_length=20),
        ),
    ]
