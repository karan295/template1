# Generated by Django 3.2.2 on 2021-05-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]