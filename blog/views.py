from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from django.views.decorators import csrf
from blog import models
from django.contrib import messages
from markdown import markdown, Markdown
from myweb.settings.base import PER_PAGE
from django import forms
from django.db.models import Q
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect

# 文章主页
def index(request):
    # 对文章列表对象进行分页, 目前可以却四嗯每页多少条数据；
    paginator = Paginator(models.Article.objects.all().order_by('-pub_time'), PER_PAGE)
    # 获取当前的页数
    page = request.GET.get('page')
    # 假设要看-1页? 总共10页， 要看12页?要做异常处理;
    try:
        # post对象拥有的方法查看源代码:Page类；
        articles = paginator.page(page)
        # 获取宗页数；
        print(paginator.num_pages)
        # 获取页数显示列表; range(1,11), 将舍page_range有100页， 如何让显示参考flask的设置；
        print(paginator.page_range)
    except (PageNotAnInteger, EmptyPage):
        # 如果传进来的时字符串， 默认去看第一页;
        articles = paginator.page(1)

    return render(request, 'blog/index.html',
                  context={'title': '博客主页',
                           'articles': articles,
                           'paginator': paginator,
                           'page_nums': paginator.page_range})


# 我觉得search，archive，tag，category用参数放在index后面
# 只显示特定分类的文章
def category(request, category_id):
    category = get_object_or_404(models.Category, id=category_id)
    articles = models.Article.objects.filter(category=category).order_by('-pub_time')
    return render(request, 'blog/index.html',
                  context={
                      'articles': articles
                  })


# 只显示特定标签的文章
def tag(request, tag_id):
    # 先找出TagId对应的tag对象；
    tag = get_object_or_404(models.Tags, id=tag_id)
    articles = models.Article.objects.filter(tags=tag).order_by('-pub_time')
    return render(request, 'blog/index.html',
                  context={
                      'articles': articles
                  })


# 按时间归档
def archive(request, year, month):  # 2018 10
    articles = models.Article.objects.filter(
        pub_time__year=year,
        pub_time__month=month
    ).order_by('-update_time')

    return render(request, 'blog/index.html',
                  context={
                      'articles': articles
                  })


# 搜索
def search(request):
    # get方法提交数据的。 如何获取get方法提交的数据;
    query = request.GET.get('query', None)  # westos
    # Q对象包装查询逻辑， 找出标题中包含query或者文章内容中包含query的博客对象;
    articles = models.Article.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))

    # 如果没有找到， 返回一个报错信息；
    if not articles:
        return render(request, 'blog/index.html',
                      context={
                          'articles': articles,
                          'message': "没有找到相关信息"
                      })
    else:
        return render(request, 'blog/index.html',
                      context={
                          'articles': articles,

                      })


# 文章细节
def detail(request, detail_id):
    article = models.Article.objects.get(id=detail_id)
    article.add_views()
    md = Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ],
        output_format='html'
    )
    article.body = md.convert(article.body)
    article.toc = md.toc
    comments = models.Comment.objects.filter(article_id=detail_id).order_by('-pub_time')
    form = CommentForm()
    return render(request, 'blog/detail.html', context={
        'article': article,
        'comments': comments,
        'form': form,
    })


# 表单
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']


# 写评论
@login_required
@csrf_exempt
def comment_add(request, detail_id):
    article = models.Article.objects.get(id=detail_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = auth.get_user(request)
            comment.save()
            return redirect(article.get_url())
        else:
            messages.error(request, 'error!')
            return render(request, 'blog/detail.html', context={
                'errors': form.errors
            })
    else:
        return redirect(article.get_url())

# Admin后台有了，不急着实现
# 添加文章标签

# 删除文章标签

# 写文章界面

# 保存文章界面

