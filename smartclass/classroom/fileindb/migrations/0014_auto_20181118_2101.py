# Generated by Django 2.0.5 on 2018-11-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileindb', '0013_auto_20181118_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examtype',
            name='exam_type',
            field=models.CharField(choices=[('3', 'PROJECT'), ('4', 'LAB'), ('5', 'END'), ('1', 'MID1'), ('2', 'MID2')], default=2, max_length=20),
        ),
    ]
