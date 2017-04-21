from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	author = models.PositiveIntegerField()
	published = models.BooleanField('Published')

	def __str__(self):
		return "{}".format(self.title)