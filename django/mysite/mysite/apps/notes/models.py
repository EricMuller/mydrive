from django.db import models

# Create your models here.


class Note(models.Model):
	titre = models.CharField(max_length=30)
	description = models.CharField(max_length=40)
	email = models.EmailField()
	documents = models.ForeignKey('Document')


class ReStText(models.Model):
	contents=models.CharField(max_length=1024)

	def __unicode__(self):
		return self.contents


class Code(models.Model):
	code_id=models.CharField(max_length=20,primary_key=True)
	libelle=models.CharField(max_length=100)

	def __unicode__(self):
		return self.libelle

	class Meta:
		abstract = True

class System(Code,models.Model):

	pass


class Document(models.Model):
	"""docstring for ClassName"""
	nom = models.CharField(max_length=30)
	path= models.CharField(max_length=512)
	contentType=models.CharField(max_length=30)

class Language(Code):
	pass

class ReSTNote(models.Model):
	titre = models.CharField(max_length=30 ,verbose_name='Titre')
	codeSystem = models.ForeignKey(System , verbose_name='systeme')
	codeLangage =	models.ForeignKey(Language, verbose_name='Langage')
	reStText = models.ForeignKey(ReStText,verbose_name='ReST Texte')



