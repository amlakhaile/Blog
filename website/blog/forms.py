from django import forms
from .models import blog_post

class Postform(forms.ModelForm):
	class Meta:
		model = blog_post
		fields = ['author', 'title', 'content']