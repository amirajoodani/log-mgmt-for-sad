# Generated by Django 3.2.12 on 2022-04-25 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20220424_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event_image/'),
        ),
    ]
