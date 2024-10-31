# Generated by Django 5.1.2 on 2024-10-30 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_uuid',
            field=models.SlugField(max_length=150, unique=True),
        ),
        migrations.AddIndex(
            model_name='wallet',
            index=models.Index(fields=['wallet_uuid'], name='wallet_api__wallet__67df5c_idx'),
        ),
    ]
