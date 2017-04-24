from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.conf import settings

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	published = models.BooleanField('Published')
	slug = models.SlugField(max_length=100)
	date_updated = models.DateTimeField()

	def __str__(self):
		return "{}".format(self.title)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)
