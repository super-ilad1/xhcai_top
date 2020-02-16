from django import template
from django.template.defaultfilters import stringfilter
import chardet
register = template.Library()

@register.filter
@stringfilter
def process(value):
    return value[0:5]

# 最重要的是在你的目标html中要添加上，
# {% load process %}
