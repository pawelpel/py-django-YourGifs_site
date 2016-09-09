from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from your_gifs.forms import CategoryForm, PostForm
from your_gifs.models import Category, Post


def add_to_context(context_dict):
    # print(1, context_dict)
    if 'categories' not in context_dict.keys():
        context_dict['categories'] = Category.objects.all()
    # print(2, context_dict)
    return context_dict


def index(request):
    context_dict = {'posts': list(Post.objects.all().order_by('-likes'))}
    return render(request, 'your_gifs/index.html', context=add_to_context(context_dict))


def show_categories(request):
    categories = Category.objects.all().order_by('name')
    posts = []
    for c in categories:
        post = Post.objects.filter(category=c).order_by('-likes')
        if post:
            posts.append(post[0])

    visible_cat = [c for c in categories if c in [p.category for p in posts]]
    return render(request, 'your_gifs/categories.html', context=add_to_context({'categories': categories,
                                                                                'posts': posts,
                                                                                'visible_cat': visible_cat}))


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

    return render(request, 'your_gifs/category.html', add_to_context(context_dict))


@login_required
def add_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return show_categories(request)
        else:
            # print(form.errors)
            pass
    return render(request, 'your_gifs/add_category.html', add_to_context({'form': form}))


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
            # print(form.errors)
            pass

    context_dict = {'form':form, 'category': category}
    return render(request, 'your_gifs/add_post.html', add_to_context(context_dict))
