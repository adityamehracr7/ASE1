# Generated by Django 2.0.5 on 2018-11-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20181118_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherpost',
            name='status',
            field=models.CharField(choices=[('publish', 'Publish'), ('draft', 'Draft')], default='publish', max_length=10),
        ),
    ]