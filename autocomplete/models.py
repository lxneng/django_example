#coding=utf8
from django.db import models

class Tag(models.Model):
    name = models.CharField(u'关键字',max_length=100)
    class Admin:
        pass
    class Meta:
        db_table= 'tags'
    def __unicode__(self):
        return  u"%s" % ( self.keyword)
