from django.contrib import admin
from drive.models import File
from drive.models import Basket
from drive.models import UploadFile
from drive.models import Repository


class FileAdmin(admin.ModelAdmin):

    list_display = [
        'name', 'path', 'contentType', 'created_at', 'updated_at',
        'version', 'repository']
    search_fields = ['name']


class BasketAdmin(admin.ModelAdmin):

    list_display = [
        'code', 'libelle', 'description', 'created_at', 'updated_at']
    search_fields = ['libelle']


class UploadFileAdmin(admin.ModelAdmin):

    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['libelle', 'created_at', 'updated_at']


class RepositoryAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'parent', 'parent', 'libelle', 'node_l', 'node_r',
        'created_at', 'updated_at']
    search_fields = ['libelle']
    ordering = ('node_l',)

   

admin.site.register(Repository, RepositoryAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(UploadFile, UploadFileAdmin)
