# Generated by Django 4.0 on 2024-03-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cno', models.IntegerField()),
                ('cName', models.CharField(max_length=100)),
                ('cContent', models.CharField(max_length=200)),
            ],
        ),
    ]
