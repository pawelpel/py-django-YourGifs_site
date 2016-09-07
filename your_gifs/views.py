from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from your_gifs.forms import *


def index(request):
    return render(request, 'your_gifs/index.html', context={})


def show_categories(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'your_gifs/categories.html', context={'categories': categories})


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        posts = Post.objects.filter(category=category)

        context_dict['posts'] = posts
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['posts'] = None

    return render(request, 'your_gifs/category.html', context_dict)


@login_required
def add_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'your_gifs/add_category.html', {'form': form})


@login_required
def add_post(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            if category:
                post = form.save(commit=False)
                post.author = request.user
                post.category = category
                post.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form':form, 'category': category}
    return render(request, 'your_gifs/add_post.html', context_dict)
