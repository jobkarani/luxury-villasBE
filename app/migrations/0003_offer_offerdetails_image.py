# Generated by Django 4.1.2 on 2023-01-02 07:27

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_price_offer_old_price_offer_complimentary1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offerDetails_image',
            field=pyuploadcare.dj.models.ImageField(default=''),
        ),
    ]
