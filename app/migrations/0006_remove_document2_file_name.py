# Generated by Django 4.1.5 on 2023-01-12 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_remove_document2_document_pdf"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="document2",
            name="file_name",
        ),
    ]