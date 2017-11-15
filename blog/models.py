from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse


# Create your models here.

class BlogPost(models.Model):
	author = models.CharField(max_length=255)
	date = models.DateTimeField(default=datetime.now)
	title = models.CharField(max_length=1024)
	slug = models.SlugField(db_index=True, max_length=1024)
	image = models.ImageField(upload_to='blog', default='blog/thumbnail-default.jpg')
	content = models.TextField()

	def get_absolute_url(self):
		return reverse('blog:detail', args=[self.id, self.slug])

	def __str__(self):
		return self.title 
