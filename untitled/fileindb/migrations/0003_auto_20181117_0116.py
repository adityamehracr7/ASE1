# Generated by Django 2.1.3 on 2018-11-16 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileindb', '0002_auto_20181117_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileindb.examtype'),
        ),
    ]