# Generated by Django 4.1.5 on 2023-01-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_document2_identity"),
    ]

    operations = [
        migrations.AddField(
            model_name="document2",
            name="file_path",
            field=models.CharField(default=34, max_length=50),
            preserve_default=False,
        ),
    ]
