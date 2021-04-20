from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post


class BlogPostSitemap(Sitemap):
    """
    ブログ記事のサイトマップ
    """
    changefreq = "never"
    priority = 0.8

    def items(self):
        return Post.objects.filter(is_public=True)

    # モデルに get_absolute_url() が定義されている場合は不要
    def location(self, obj):
        return reverse('blog:post_detail', args=[obj.pk])

    def lastmod(self, obj):
        return obj.published_at


class StaticViewSitemap(Sitemap):
    """
    静的ページのサイトマップ
    """
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return ['blog:index', 'blog:category_list', 'blog:tag_list']

    def location(self, item):
        return reverse(item)