# Generated by Django 4.0.4 on 2022-07-03 02:58

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
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=100)),
                ('quartier', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('profil', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membre', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
