# Generated by Django 4.1 on 2022-12-15 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cook", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="Recipe",),
    ]