# Generated by Django 4.2.4 on 2023-08-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeapi', '0011_remove_placecomment_user_id_placecomment_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeimage',
            name='username',
            field=models.CharField(default=1, max_length=14),
            preserve_default=False,
        ),
    ]
