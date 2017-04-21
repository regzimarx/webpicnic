from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPostForm

# Create your views here.
def index(request):
	posts_list = Post.objects.filter(published=True)
	return_data = {'posts':posts_list}
	return render(request, 'posts/index.html', return_data)

def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        form.save()
        return redirect('/account')
    else:
        form = AddPostForm()
        return_data = {'form':form, 'author':request.user.id}
        return render(request, 'posts/add-post.html', return_data)