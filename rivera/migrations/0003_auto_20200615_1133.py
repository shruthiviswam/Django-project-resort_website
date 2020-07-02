# Generated by Django 3.0.6 on 2020-06-15 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rivera', '0002_auto_20200611_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='guests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Guests',
            },
        ),
        migrations.AddField(
            model_name='members',
            name='upload_file',
            field=models.FileField(default='NA', upload_to='documents,'),
        ),
        migrations.AlterField(
            model_name='members',
            name='number',
            field=models.CharField(max_length=10),
        ),
    ]