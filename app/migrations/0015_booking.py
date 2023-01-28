# Generated by Django 4.1.5 on 2023-01-26 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0014_rename_video_country_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('guests', models.IntegerField()),
                ('room_type', models.CharField(max_length=100)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('confirmation_number', models.CharField(max_length=20, unique=True)),
                ('special_requests', models.TextField(blank=True, null=True)),
                ('booking_status', models.CharField(default='pending', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('villa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.villa')),
            ],
        ),
    ]