# Generated by Django 4.0.4 on 2022-07-05 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_user', '0006_alter_membre_description_alter_membre_fonction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='quartier',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='membre',
            name='ville',
            field=models.CharField(max_length=100),
        ),
    ]
