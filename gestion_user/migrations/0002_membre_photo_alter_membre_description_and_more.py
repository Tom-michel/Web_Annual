# Generated by Django 4.0.4 on 2022-07-03 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membre',
            name='photo',
            field=models.ImageField(blank=True, default='pp.jpeg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='membre',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='membre',
            name='profil',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
