from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPostForm, EditPostForm
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def index(request, page):
    posts_list = Post.objects.filter(published=True).order_by('-date_created')
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginator.page(paginator.num_pages)
    return_data = {'posts':paginated_posts}
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

def edit_post(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        published = request.POST.get('published')
        post.date_updated = datetime.now()
        if published is not None:
            post.published = True
        else:
            post.published = False
        post.save()
        return redirect('account')
    else:
        form = EditPostForm()
        post = Post.objects.get(id=id)
        return_data = {'form':form, 'post':post, 'author': request.user.id}
        return render(request, 'posts/edit-post.html', return_data)

def view_post(request, slug):
    post = Post.objects.get(slug=slug)
    return_data = {'post': post}
    return render(request, 'posts/post.html', return_data)

def search_post(request):
    s = request.GET.get('s')
    posts = Post.objects.filter(Q(title__contains=s) | Q(content__contains=s))
    return_data = {'posts': posts}
    return render(request, 'posts/search.html', return_data)