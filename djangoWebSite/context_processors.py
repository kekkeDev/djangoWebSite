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
    # GoogleアナリティクスのトラッキングIDをsettings.pyから取得する
    # settings.py内に、GOOGLE_ANALYTICS_TRACKING_ID='自分のトラッキングID'を書き込んでおく
    ga_tracking_id = getattr(settings, 'GOOGLE_ANALYTICS_TRACKING_ID', False)

    # DEBUG=FalseかつGoogleアナリティクスのトラッキングIDを取得できたら、
    # テンプレート内で'GOOGLE_ANALYTICS_TRACKING_ID'という変数を利用できるようにする
    if not settings.DEBUG and ga_tracking_id:
        return {
            'GOOGLE_ANALYTICS_TRACKING_ID': ga_tracking_id,
        }
    return {}