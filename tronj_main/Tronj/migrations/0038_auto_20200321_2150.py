# Generated by Django 2.2.3 on 2020-03-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tronj', '0037_auto_20200321_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='Question1',
            field=models.CharField(default='what is your aim?', max_length=150),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='Question3',
            field=models.CharField(default='Why you want this Job?', max_length=150),
        ),
    ]
