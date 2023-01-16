from django.db import models
Category = (
    ('sales','sales'),
    ('procurement', 'procurement'),)

Types = (
    ('producer','producer'),
    ('brand owner','brand owner'),
    ('importer', 'importer'),)

class BlobField(models.Field):
    description = "Blob"
    def db_type(self, connection):
        return 'blob'

class Document(models.Model):
    email = models.EmailField(max_length=42)
    password = models.CharField(max_length=75)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'document'

class Document2(models.Model):
    identity = models.CharField(max_length=75)
    types = models.CharField(max_length=20, choices=Types, default='producer')
    category = models.CharField(max_length=20, choices=Category, default='sales')
    # file_name = models.CharField(max_length=50)
    document_excel = BlobField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'document2'