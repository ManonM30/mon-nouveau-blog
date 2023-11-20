# Generated by Django 4.1 on 2023-11-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarseilleInsiderApp', '0009_remove_achetepack_nombre_alter_pack_nombre_loisirs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loisir',
            old_name='name_voie',
            new_name='nom_voie',
        ),
        migrations.AddField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='client',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
