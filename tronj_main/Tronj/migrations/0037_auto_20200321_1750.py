# Generated by Django 2.2.3 on 2020-03-21 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tronj', '0036_auto_20200321_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_details',
            old_name='Location',
            new_name='Address',
        ),
    ]
