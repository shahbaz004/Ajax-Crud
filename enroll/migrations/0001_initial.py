# Generated by Django 3.2.7 on 2021-09-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.CharField(max_length=11, verbose_name='Roll No')),
                ('mobile', models.CharField(max_length=13)),
                ('program', models.CharField(max_length=10)),
            ],
        ),
    ]
