from django.shortcuts import render, redirect
from .models import blog_post
from .forms import Postform
from django.contrib import messages


def index(request):
	all_posts = blog_post.objects.all
	return render(request, 'index.html', {'all':all_posts})

def post(request):
	if request.method == "POST":
		form = Postform(request.POST or None)
		if form.is_valid:
			form.save()
		messages.success(request, ('Your blog has been posted successfully!'))
		return redirect('index')
	else:
		return render(request, 'post.html', {})