# Generated by Django 3.2.24 on 2024-03-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='wich',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('countary', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='pich',
            name='id',
            field=models.IntegerField(max_length=20, primary_key=True, serialize=False),
        ),
    ]