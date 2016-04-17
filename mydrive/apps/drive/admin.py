from django.contrib import admin
from drive.models import Document
from drive.models import Basket
from drive.models import UploadFile
from drive.models import DriveNode


class DocumentAdmin(admin.ModelAdmin):

    list_display = [
        'name', 'path', 'contentType', 'created_at', 'updated_at',
        'version', 'folder']
    search_fields = ['name']


class BasketAdmin(admin.ModelAdmin):

    list_display = [
        'code', 'libelle', 'description', 'created_at', 'updated_at']
    search_fields = ['libelle']


class UploadFileAdmin(admin.ModelAdmin):

    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['libelle', 'created_at', 'updated_at']


class DriveNodeAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'parent', 'parent', 'libelle', 'node_l', 'node_r',
        'created_at', 'updated_at']
    search_fields = ['libelle']
    ordering = ('node_l',)

admin.site.register(DriveNode, DriveNodeAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(UploadFile, UploadFileAdmin)
