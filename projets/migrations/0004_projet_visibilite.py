# Generated by Django 4.0.4 on 2022-07-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '0003_alter_tache_progression_projet'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='visibilite',
            field=models.CharField(choices=[('public', 'public'), ('private', 'private')], default='public', max_length=200),
        ),
    ]
