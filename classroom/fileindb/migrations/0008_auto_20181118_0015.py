# Generated by Django 2.0.5 on 2018-11-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileindb', '0007_auto_20181118_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examtype',
            name='exam_type',
            field=models.CharField(choices=[(4, 'PROJECT'), (5, 'END_SEM'), (1, 'MID1'), (3, 'LAB'), (2, 'MID2')], default=2, max_length=20),
        ),
    ]
