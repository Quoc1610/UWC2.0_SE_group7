# Generated by Django 4.1.3 on 2022-11-12 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_transportation_id_alter_transportation_name'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='mcp_janitor',
            constraint=models.UniqueConstraint(fields=('janitor', 'mcp'), name='mcp_janitor'),
        ),
    ]
