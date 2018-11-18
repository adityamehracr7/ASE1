# Generated by Django 2.1.3 on 2018-11-18 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_dash', '0018_auto_20181118_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examtype',
            name='exam_type',
            field=models.CharField(choices=[('project', 'PROJECT'), ('end', 'END'), ('mid1', 'MID1'), ('mid2', 'MID2'), ('lab', 'LAB')], default='mid1', max_length=20),
        ),
        migrations.AlterField(
            model_name='studentattendence',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_dash.table'),
        ),
    ]