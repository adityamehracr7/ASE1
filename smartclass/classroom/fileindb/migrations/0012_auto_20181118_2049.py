# Generated by Django 2.0.5 on 2018-11-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileindb', '0011_auto_20181118_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examtype',
            name='exam_type',
            field=models.CharField(choices=[('5', 'END'), ('1', 'MID1'), ('2', 'MID2'), ('4', 'LAB'), ('3', 'PROJECT')], default=2, max_length=20),
        ),
    ]
