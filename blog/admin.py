from django.contrib import admin
from django.contrib.sites.models import Site
from blog.models import SiteDetail, Category, Tag, Post, ContentImage, Comment, Reply


class ContentImageInline(admin.TabularInline):
    model = ContentImage
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ContentImageInline,
    ]

class SiteDetailInline(admin.StackedInline):
    """サイト詳細情報のインライン"""
    model = SiteDetail

class SiteAdmin(admin.ModelAdmin):
    """Siteモデルを、管理画面でSiteDetailもインラインで表示できるように"""
    inlines = [SiteDetailInline]

admin.site.unregister(Site)
admin.site.register(Site, SiteAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Reply)
