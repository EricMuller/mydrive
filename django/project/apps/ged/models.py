from django.db import models
# from django.utils import timezone


class Basket(models.Model):
    code = models.CharField(primary_key=True, max_length=30)
    libelle = models.CharField(max_length=30)
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def create(cls, code, libelle, description):
        basket = cls(code=code, libelle=libelle, description=description)
        return basket

    def __str__(self):
        return self.libelle


class Document(models.Model):

    """docstring for ClassName"""
    name = models.CharField(max_length=256)
    path = models.CharField(max_length=512)
    contentType = models.CharField(max_length=30)
    version = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    basket = models.ForeignKey(Basket, verbose_name='Basket', default=None)

    @classmethod
    def create(cls, name, path, contentType, version, basket):
        document = cls(
            name=name, path=path, contentType=contentType,
            version=version, basket=basket)
        return document


class UploadFile(models.Model):

    name = models.CharField(max_length=256, default=None)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Folder(models.Model):
    
    name = models.CharField(max_length=256)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

