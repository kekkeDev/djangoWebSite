from django.db.models import Count, Q
from django.conf import settings
from blog.models import Category, Tag


def common(request):
    context = {
        'categories': Category.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'tags': Tag.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
    }
    return context

def google_analytics(request):
    """
    DEBUG=Falseの場合に、GoogleアナリティクスのトラッキングIDを返す
    """
    if not settings.DEBUG and settings.GOOGLE_ANALYTICS_TRACKING_ID:
        return {
            'GOOGLE_ANALYTICS_TRACKING_ID': settings.GOOGLE_ANALYTICS_TRACKING_ID,
        }
    return {}