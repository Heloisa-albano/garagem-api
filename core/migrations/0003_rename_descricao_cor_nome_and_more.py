# Generated by Django 5.0.2 on 2024-04-02 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_acessorio_categoria_cor_marca"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cor",
            old_name="descricao",
            new_name="nome",
        ),
        migrations.RenameField(
            model_name="marca",
            old_name="descricao",
            new_name="nome",
        ),
    ]
