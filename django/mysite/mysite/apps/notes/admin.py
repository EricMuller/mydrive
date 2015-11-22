from django import forms
from django.contrib import admin
from django.forms import TextInput
from django.forms import Textarea

#admin.site.register(Rules, RulesAdmin)
from mysite.apps.notes.models import System
from mysite.apps.notes.models import Language
from mysite.apps.notes.models import ReStText
from mysite.apps.notes.models import ReSTNote


class SystemAdmin(admin.ModelAdmin):
	list_display = [ 'code_id', 'libelle' ]
	search_fields = [ 'code_id' ]
   
class LanguageAdmin(admin.ModelAdmin):
	list_display = [ 'code_id', 'libelle' ]
	search_fields = [ 'code_id' ]

class ReSTTextForm(forms.ModelForm):
    contents = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    class Meta:
    	fields = ('id', 'contents',)
        model = ReStText

class ReStTextAdmin(admin.ModelAdmin):
	form = ReSTTextForm
	list_display = [ 'id','contents', ]
	search_fields = [ 'contents' ]

class ReSTNoteAdmin(admin.ModelAdmin):
	
	list_display = [ 'titre', 'codeSystem' ,'codeLangage','reStText']
	search_fields = [ 'titre' ]


admin.site.register(System, SystemAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(ReStText, ReStTextAdmin)
admin.site.register(ReSTNote, ReSTNoteAdmin)
