# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rubro'
        db.create_table(u'contribuyentes_rubro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.IntegerField')()),
            ('rubro', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('alicuota', self.gf('django.db.models.fields.FloatField')()),
            ('ut', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'contribuyentes', ['Rubro'])

        # Adding model 'Contribuyente'
        db.create_table(u'contribuyentes_contribuyente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_contrato', self.gf('django.db.models.fields.IntegerField')()),
            ('num_identificacion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('telf', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('representante', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('cedula_rep', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('capital', self.gf('django.db.models.fields.FloatField')()),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'contribuyentes', ['Contribuyente'])

        # Adding M2M table for field rubro on 'Contribuyente'
        m2m_table_name = db.shorten_name(u'contribuyentes_contribuyente_rubro')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contribuyente', models.ForeignKey(orm[u'contribuyentes.contribuyente'], null=False)),
            ('rubro', models.ForeignKey(orm[u'contribuyentes.rubro'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contribuyente_id', 'rubro_id'])

        # Adding model 'Licencia'
        db.create_table(u'contribuyentes_licencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('control', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('emision', self.gf('django.db.models.fields.DateField')()),
            ('valido', self.gf('django.db.models.fields.DateField')()),
            ('contribuyente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contribuyentes.Contribuyente'])),
        ))
        db.send_create_signal(u'contribuyentes', ['Licencia'])


    def backwards(self, orm):
        # Deleting model 'Rubro'
        db.delete_table(u'contribuyentes_rubro')

        # Deleting model 'Contribuyente'
        db.delete_table(u'contribuyentes_contribuyente')

        # Removing M2M table for field rubro on 'Contribuyente'
        db.delete_table(db.shorten_name(u'contribuyentes_contribuyente_rubro'))

        # Deleting model 'Licencia'
        db.delete_table(u'contribuyentes_licencia')


    models = {
        u'contribuyentes.contribuyente': {
            'Meta': {'object_name': 'Contribuyente'},
            'capital': ('django.db.models.fields.FloatField', [], {}),
            'cedula_rep': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_contrato': ('django.db.models.fields.IntegerField', [], {}),
            'modificado': ('django.db.models.fields.DateField', [], {}),
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