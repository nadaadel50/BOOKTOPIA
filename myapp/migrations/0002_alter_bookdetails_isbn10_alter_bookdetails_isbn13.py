# Generated by Django 5.0.4 on 2024-05-07 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetails',
            name='isbn10',
            field=models.CharField(default='N/A', max_length=10),
        ),
        migrations.AlterField(
            model_name='bookdetails',
            name='isbn13',
            field=models.CharField(default='N/A', max_length=13),
        ),
    ]
