# Generated by Django 4.0.4 on 2022-07-09 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='etat',
            field=models.CharField(choices=[('etat 1', 'etat1'), ('etat 2', 'etat2'), ('etat 3', 'etat3')], default='etat 1', max_length=20),
        ),
    ]
