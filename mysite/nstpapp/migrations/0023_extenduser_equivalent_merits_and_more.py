# Generated by Django 4.1.2 on 2022-10-31 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0022_extenduser_td10_dem_extenduser_td11_dem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='equivalent_merits',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='equivalent_merits2',
            field=models.CharField(default='', max_length=20),
        ),
    ]
