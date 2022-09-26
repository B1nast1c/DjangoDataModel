# Generated by Django 4.1.1 on 2022-09-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Modelo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="rol",
            field=models.CharField(
                choices=[
                    ("ADMIN", "Admin"),
                    ("CLIENT", "Client"),
                    ("GERENT", "Gerent"),
                ],
                default="CLIENT",
                max_length=16,
            ),
        ),
    ]
