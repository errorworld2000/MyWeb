from django.urls import path, re_path

from blog import views

urlpatterns = [
    # 默认带有/？page=1
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('comment_add/<int:detail_id>/', views.comment_add, name='comment_add'),
    path('detail/<int:detail_id>/', views.detail, name='detail'),
    re_path(r'^archive/(?P<year>\d{4})/(?P<month>\d+)/$', views.archive, name='archive'),
    re_path(r"^category/(?P<category_id>\d+)/$", views.category, name="category"),
    re_path(r"^tag/(?P<tag_id>\d+)/$", views.tag, name="tag"),
]
app_name = 'blog'
