# Generated by Django 4.1.1 on 2022-09-25 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0008_alter_certification_commandant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='school_year',
            name='date_generated',
            field=models.CharField(default='', max_length=40),
        ),
    ]
