# Generated by Django 4.0.4 on 2022-07-23 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '0005_alter_projet_updated_alter_tache_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='description',
            field=models.TextField(blank=True, default='Brève description du projet', max_length=200),
        ),
    ]
