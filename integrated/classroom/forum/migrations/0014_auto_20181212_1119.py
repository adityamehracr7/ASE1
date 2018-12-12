# Generated by Django 2.0.5 on 2018-12-12 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0013_notifications_is_read'),
    ]

    operations = [
        migrations.CreateModel(
            name='otp_verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('otp', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='teacherpost',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='publish', max_length=10),
        ),
    ]