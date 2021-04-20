from django import template
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code', 'extra', 'admonition', 'sane_lists', 'toc'])
#
# def markdown_to_html(self):
#     """Markdown を HTML に変換して出力
#     さらに拡張機能を使用して目次を自動生成する"""
#     md = md.Markdown(
#         extensions=['extra', 'admonition', 'sane_lists', 'toc'])
#     html = md.convert(self.content)
#     return html