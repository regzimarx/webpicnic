from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
	posts_list = Post.objects.all()
	return_data = {'posts':posts_list}
	return render(request, 'posts/index.html', return_data)