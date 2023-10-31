from django.contrib import admin

from blog.models import Article, Category, Tags, Comment


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_time', 'update_time',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Comment)
