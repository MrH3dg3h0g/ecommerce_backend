# Generated by Django 4.1.2 on 2022-11-18 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_options_optionsvalue_productvariants'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductVariants',
        ),
    ]
