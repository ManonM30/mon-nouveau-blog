# Generated by Django 4.1 on 2023-11-15 20:05

import MarseilleInsiderApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarseilleInsiderApp', '0003_catégorie_client_fournisseur_pack_prix_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='mdp_utilisateur',
            field=models.CharField(help_text='Le mot de passe doit contenir au moins 1 majuscule, 1 chiffre et 1 caratère spécial', max_length=20, unique=True, validators=[MarseilleInsiderApp.models.validate_mdp], verbose_name='Mot de passe utilisateur'),
        ),
    ]
