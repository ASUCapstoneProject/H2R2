# Generated by Django 4.1.5 on 2023-03-13 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basewater', '0014_alter_waterquality_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterquality',
            name='company',
            field=models.CharField(default='Default Company', max_length=200),
        ),
    ]