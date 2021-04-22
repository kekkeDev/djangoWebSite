from django.db.models import Count, Q
from django.conf import settings
from blog.models import Category, Tag, SiteDetail


def common(request):
    context = {
        'categories': Category.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'tags': Tag.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'site_detail_1': SiteDetail.objects.get(pk=1),
    }
    return context

def settings_param(request):
    """
    DEBUG=Falseの場合に、GoogleアナリティクスのトラッキングIDを返す
    """
    return {
        'is_debug': settings.DEBUG,
    }
