from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mdeditor.fields import MDTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField('分类', max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField('标签', max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    intro = models.CharField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类', default='others')
    tags = models.ManyToManyField(Tags, blank=True, verbose_name='标签')
    body = MDTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者', default='anonymity')
    pub_time = models.DateTimeField('发布时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    views = models.PositiveIntegerField(default=0, verbose_name="阅读量")

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("blog:detail", kwargs={'detail_id': self.id})

    def add_views(self):
        self.views += 1
        self.save(update_fields=['views'])


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]
