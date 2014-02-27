# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cuota'
        db.create_table(u'liquidaciones_cuota', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orden', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'liquidaciones', ['Cuota'])


    def backwards(self, orm):
        # Deleting model 'Cuota'
        db.delete_table(u'liquidaciones_cuota')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'contribuyentes.contribuyente': {
            'Meta': {'object_name': 'Contribuyente'},
            'capital': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'cedula_rep': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'creado': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_contrato': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'modificado': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'num_identificacion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'representante': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'rubro': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['contribuyentes.Rubro']", 'null': 'True', 'blank': 'True'}),
            'telf': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'contribuyentes.rubro': {
            'Meta': {'object_name': 'Rubro'},
            'alicuota': ('django.db.models.fields.FloatField', [], {}),
            'codigo': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rubro': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'ut': ('django.db.models.fields.IntegerField', [], {})
        },
        u'liquidaciones.cuota': {
            'Meta': {'object_name': 'Cuota'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'liquidaciones.impuesto': {
            'Meta': {'object_name': 'Impuesto'},
            'codigo': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.CharField', [], {'default': "'Sin definir'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'liquidaciones.liquidacion': {
            'Meta': {'object_name': 'Liquidacion'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'emision': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impuesto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['liquidaciones.Impuesto']"}),
            'intereses': ('django.db.models.fields.FloatField', [], {}),
            'liquidador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'recargo': ('django.db.models.fields.FloatField', [], {}),
            'trimestre': ('django.db.models.fields.IntegerField', [], {})
        },
        u'liquidaciones.liquidacion2': {
            'Meta': {'object_name': 'Liquidacion2'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'contribuyente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contribuyentes.Contribuyente']"}),
            'deposito': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'emision': ('django.db.models.fields.DateField', [], {}),
            'fecha_pago': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liquidador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'modopago': ('django.db.models.fields.CharField', [], {'default': "'DP'", 'max_length': '2'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'vencimiento': ('django.db.models.fields.DateField', [], {})
        },
        u'liquidaciones.pago': {
            'Meta': {'object_name': 'Pago'},
            'contribuyente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contribuyentes.Contribuyente']"}),
            'credito_fiscal': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True'}),
            'deposito': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'descuento': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True'}),
            'emision': ('django.db.models.fields.DateField', [], {}),
            'fecha_pago': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impuesto': ('django.db.models.fields.FloatField', [], {}),
            'intereses': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True'}),
            'liquidacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['liquidaciones.Liquidacion']", 'null': 'True'}),
            'num_liquidacion': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'recargo': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True'}),
            'vencimiento': ('django.db.models.fields.DateField', [], {})
        },
        u'liquidaciones.pago2': {
            'Meta': {'object_name': 'Pago2'},
            'cancelado': ('django.db.models.fields.FloatField', [], {}),
            'credito_fiscal': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True'}),
            'descuento': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impuesto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['liquidaciones.Impuesto']"}),
            'intereses': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'liquidacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['liquidaciones.Liquidacion2']"}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'recargo': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'SND'", 'max_length': '3'}),
            'trimestres': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'ut': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['liquidaciones.UT']"})
        },
        u'liquidaciones.ut': {
            'Meta': {'object_name': 'UT'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valor': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['liquidaciones']
