# Generated by Django 4.0.4 on 2022-07-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_user', '0007_alter_membre_quartier_alter_membre_ville'),
    ]

    operations = [
        migrations.AddField(
            model_name='membre',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
