# Generated by Django 4.1.2 on 2022-12-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0005_alter_extenduser_proof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='proof',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
