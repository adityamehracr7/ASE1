# Generated by Django 2.0.5 on 2018-12-12 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0014_auto_20181212_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherpost',
            name='status',
            field=models.CharField(choices=[('publish', 'Publish'), ('draft', 'Draft')], default='publish', max_length=10),
        ),
    ]