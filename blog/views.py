from django.shortcuts import render
from .models import Post

# Create your views here.
from django.http import HttpResponse


def Home(request):
	content = { 'posts': Post.objects.all() }
	return render(request, 'blog/Home.html', content)


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
