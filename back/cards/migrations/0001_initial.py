# Generated by Django 4.2.13 on 2024-05-16 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('image_url', models.TextField(blank=True)),
                ('annual_fee1', models.IntegerField(blank=True, null=True)),
                ('annual_fee2', models.IntegerField(blank=True, null=True)),
                ('record', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_owner', models.BooleanField(default=False)),
                ('live_alone', models.BooleanField(default=False)),
                ('student', models.BooleanField(default=False)),
                ('baby', models.BooleanField(default=False)),
                ('pets', models.BooleanField(default=False)),
                ('easy_pay', models.BooleanField(default=False)),
                ('healthcare', models.BooleanField(default=False)),
                ('telecom', models.BooleanField(default=False)),
                ('sports', models.BooleanField(default=False)),
                ('shopping', models.BooleanField(default=False)),
                ('friends', models.BooleanField(default=False)),
                ('fitness', models.BooleanField(default=False)),
                ('movie', models.BooleanField(default=False)),
                ('travel_inter', models.BooleanField(default=False)),
                ('trevel_dome', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.card')),
            ],
        ),
    ]
