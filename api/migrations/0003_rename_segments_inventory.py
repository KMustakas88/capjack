# Generated by Django 3.2.9 on 2021-12-16 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_inventory_segments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Segments',
            new_name='Inventory',
        ),
    ]
