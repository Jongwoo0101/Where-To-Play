# Generated by Django 4.2.4 on 2023-08-24 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_levels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phonenumber',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
