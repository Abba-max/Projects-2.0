# Generated by Django 5.1 on 2024-08-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('free', models.IntegerField()),
                ('rating', models.CharField(max_length=5)),
            ],
        ),
    ]
