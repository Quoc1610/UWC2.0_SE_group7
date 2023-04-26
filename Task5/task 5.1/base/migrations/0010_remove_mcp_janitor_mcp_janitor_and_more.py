# Generated by Django 4.1.3 on 2022-11-12 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_mcp_janitor_mcp_janitor'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='mcp_janitor',
            name='mcp_janitor',
        ),
        migrations.AddConstraint(
            model_name='mcp_janitor',
            constraint=models.UniqueConstraint(fields=('janitor', 'mcp', 'work_date'), name='mcp_janitor_date'),
        ),
    ]