# Generated by Django 3.0.6 on 2020-06-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rivera', '0007_auto_20200622_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='arrive',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='guest',
            name='bedding',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='guest',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='guest',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='guest',
            name='depart',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='guest',
            name='mail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='guest',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='guest',
            name='room',
            field=models.CharField(max_length=10),
        ),
    ]
