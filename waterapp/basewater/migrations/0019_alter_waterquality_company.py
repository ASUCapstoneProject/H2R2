# Generated by Django 4.1.5 on 2023-03-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basewater', '0018_auto_20230313_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterquality',
            name='company',
            field=models.CharField(max_length=200),
        ),
    ]
