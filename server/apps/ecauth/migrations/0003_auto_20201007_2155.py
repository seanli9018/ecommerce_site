# Generated by Django 3.1.1 on 2020-10-08 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecauth', '0002_auto_20201002_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecuser',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]