# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=30)),
                ('path', models.CharField(max_length=512)),
                ('contentType', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('libelle', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('documents', models.ForeignKey(to='notes.Document')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReSTNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=30, verbose_name=b'Titre')),
                ('codeLangage', models.ForeignKey(verbose_name=b'Langage', to='notes.Language')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReStText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('code_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('libelle', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='restnote',
            name='codeSystem',
            field=models.ForeignKey(verbose_name=b'systeme', to='notes.System'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restnote',
            name='reStText',
            field=models.ForeignKey(verbose_name=b'ReST Texte', to='notes.ReStText'),
            preserve_default=True,
        ),
    ]
