# Generated by Django 3.2.8 on 2021-10-30 02:30

from django.db import migrations, models
import utilisateurs.models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo_profile',
            field=models.ImageField(blank=True, upload_to=utilisateurs.models.renomer_image),
        ),
    ]