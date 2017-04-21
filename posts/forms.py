from django import forms
from django.forms import ModelForm
from .models import Post

class AddPostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'author', 'published']