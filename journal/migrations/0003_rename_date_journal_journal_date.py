# Generated by Django 4.2.2 on 2023-06-24 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_rename_public_journal_is_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='date',
            new_name='journal_date',
        ),
    ]