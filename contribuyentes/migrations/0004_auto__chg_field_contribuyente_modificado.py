# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Contribuyente.modificado'
        db.alter_column(u'contribuyentes_contribuyente', 'modificado', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'Contribuyente.modificado'
        db.alter_column(u'contribuyentes_contribuyente', 'modificado', self.gf('django.db.models.fields.DateField')())

    models = {
        u'contribuyentes.contribuyente': {
            'Meta': {'object_name': 'Contribuyente'},
            'capital': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'cedula_rep': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_contrato': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'modificado': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'num_identificacion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'representante': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'rubro': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['contribuyentes.Rubro']", 'null': 'True', 'symmetrical': 'False'}),
            'telf': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'contribuyentes.licencia': {
            'Meta': {'object_name': 'Licencia'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'contribuyente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contribuyentes.Contribuyente']"}),
            'control': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'emision': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'valido': ('django.db.models.fields.DateField', [], {})
        },
        u'contribuyentes.rubro': {
            'Meta': {'object_name': 'Rubro'},
            'alicuota': ('django.db.models.fields.FloatField', [], {}),
            'codigo': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rubro': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'ut': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['contribuyentes']