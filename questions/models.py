from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(unique = True)
    img1 = models.ImageField(upload_to = 'q_img')
    img2 = models.ImageField(upload_to = 'q_img', blank = True, null = True)
    level = models.IntegerField(unique = True)
    clue = models.TextField(blank = True, null = True)
    answer = models.CharField(max_length = 50)
    numsolved = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return str(self.level)
        
    def get_absolute_url(self):
        return reverse('questions:q_view', kwargs = { "slug" : self.slug }) 