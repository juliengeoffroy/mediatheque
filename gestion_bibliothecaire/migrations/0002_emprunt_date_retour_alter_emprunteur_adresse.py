# Generated by Django 5.1.7 on 2025-04-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_bibliothecaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprunt',
            name='date_retour',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprunteur',
            name='adresse',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
