# Generated by Django 5.0.4 on 2024-06-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_bookdetails_pdf_alter_bookdetails_authorimage_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdetails',
            name='no_of_borrow',
            field=models.BigIntegerField(default=0),
        ),
    ]
