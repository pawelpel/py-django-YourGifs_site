from django.conf.urls import url
from your_gifs import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^your_gifs/', views.index, name='index'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^categories/(?P<req_form_other_site>[01])*/', views.show_categories, name='show_categories'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_post/', views.add_post, name='add_post'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
]