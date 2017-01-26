from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    level = models.IntegerField()
    points = models.FloatField()
    status = models.IntegerField()
    rank = models.IntegerField()    
    
    class Meta:
        ordering = ('-level','points')    
    def __unicode__(self):
        return self.user.username
    
