# Generated by Django 4.1.5 on 2023-03-03 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('image_toper', pyuploadcare.dj.models.ImageField()),
                ('video_url', models.URLField(blank=True, default='', null=True)),
                ('catchy_phrase', models.CharField(max_length=100)),
                ('description1', models.TextField(max_length=1500)),
                ('description2', models.TextField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('heading', models.TextField(max_length=100)),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('catchy_phrase', models.CharField(default='', max_length=100)),
                ('description', models.TextField(max_length=4000)),
                ('timeline', models.TextField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('info1', models.TextField(default='', max_length=100)),
                ('gallery1', pyuploadcare.dj.models.ImageField(blank=True, default='', null=True)),
                ('gallery2', pyuploadcare.dj.models.ImageField(blank=True, default='', null=True)),
                ('gallery3', pyuploadcare.dj.models.ImageField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Villa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('price', models.FloatField()),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('image2', pyuploadcare.dj.models.ImageField(blank=True, null=True)),
                ('image3', pyuploadcare.dj.models.ImageField(blank=True, null=True)),
                ('image4', pyuploadcare.dj.models.ImageField(blank=True, null=True)),
                ('heading', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=4000)),
                ('feature1', models.TextField(max_length=500)),
                ('feature2', models.TextField(blank=True, max_length=500)),
                ('feature3', models.TextField(blank=True, max_length=500)),
                ('feature4', models.TextField(blank=True, max_length=500)),
                ('feature5', models.TextField(blank=True, max_length=500)),
                ('check_in', models.TimeField(blank=True, null=True)),
                ('check_out', models.TimeField(blank=True, null=True)),
                ('complimentary1', models.TextField(blank=True, max_length=500)),
                ('complimentary2', models.TextField(blank=True, max_length=500)),
                ('is_available', models.BooleanField(default=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('email', models.EmailField(max_length=256, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('offerDetails_image', pyuploadcare.dj.models.ImageField(default='')),
                ('old_price', models.FloatField()),
                ('description', models.TextField(max_length=4000)),
                ('inclusion1', models.TextField(default='', max_length=500)),
                ('inclusion2', models.TextField(blank=True, max_length=500)),
                ('inclusion3', models.TextField(blank=True, max_length=500)),
                ('inclusion4', models.TextField(blank=True, max_length=500)),
                ('inclusion5', models.TextField(blank=True, max_length=500)),
                ('complimentary1', models.TextField(blank=True, max_length=500)),
                ('complimentary2', models.TextField(blank=True, max_length=500)),
                ('complimentary3', models.TextField(blank=True, max_length=500)),
                ('complimentary4', models.TextField(blank=True, max_length=500)),
                ('term1', models.TextField(blank=True, max_length=500)),
                ('term2', models.TextField(blank=True, max_length=500)),
                ('term3', models.TextField(blank=True, max_length=500)),
                ('term4', models.TextField(blank=True, max_length=500)),
                ('term5', models.TextField(blank=True, max_length=500)),
                ('country', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.country')),
                ('villa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.villa')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tag'),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=4000)),
                ('villa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.villa')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=256, null=True)),
                ('phone', models.CharField(default='', max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('guestsnumber', models.IntegerField()),
                ('special_requests', models.TextField(blank=True, null=True)),
                ('villa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.villa')),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_cover', pyuploadcare.dj.models.ImageField(blank=True, default='', null=True)),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('heading', models.CharField(max_length=100)),
                ('text1', models.TextField(max_length=3000)),
                ('text2', models.TextField(default='', max_length=3000, null=True)),
                ('text3', models.TextField(default='', max_length=3000, null=True)),
                ('tag', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.tag')),
            ],
        ),
    ]
