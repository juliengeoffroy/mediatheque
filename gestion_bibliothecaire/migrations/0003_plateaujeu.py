# Generated by Django 5.1.7 on 2025-04-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_bibliothecaire', '0002_emprunt_date_retour_alter_emprunteur_adresse'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlateauJeu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
    ]
