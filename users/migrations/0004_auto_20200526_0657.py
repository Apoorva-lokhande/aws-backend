# Generated by Django 3.0.6 on 2020-05-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200526_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutevents',
            name='registerenddate',
            field=models.CharField(default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='teamreg',
            name='fullname',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
