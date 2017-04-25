from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPostForm, EditPostForm
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import Http404
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'posts/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        posts_list = Post.objects.filter(published=True)
        paginator = Paginator(posts_list, 5)
        page = kwargs['page']
        try:
            paginated_posts = paginator.page(page)
        except PageNotAnInteger:
            paginated_posts = paginator.page(1)
        except EmptyPage:
            paginated_posts = paginator.page(paginator.num_pages)
        context['posts'] = paginated_posts
        return context

class ViewPostView(TemplateView):
    template_name = 'posts/post.html'

    def get_context_data(self, **kwargs):
        context = super(ViewPostView, self).get_context_data(**kwargs)
        post = Post.objects.get(slug=kwargs['slug'])
        context['post'] = post
        return context

def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
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

def search_post(request):
    try:
        if request.GET.get('s'):
            s = request.GET.get('s')
            posts_list = Post.objects.filter(Q(title__contains=s) | Q(content__contains=s))
            return_data = {'posts': posts_list}
        elif request.GET.get('s_date'):
            search_date = datetime.strptime(request.GET.get('s_date'), '%Y-%m-%d')
            posts_list_by_date = Post.objects.filter(date_created=search_date)
            return_data = {'posts': posts_list_by_date}
        else:
            posts = Post.objects.all()
            return_data = {'posts':posts}
    except Post.DoesNotExist:
        raise Http404('No post matched your query')
    return render(request, 'posts/search.html', return_data)