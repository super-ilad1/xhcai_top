from django import template
from django.template.defaultfilters import stringfilter
import chardet
register = template.Library()

@register.filter
@stringfilter
def process(value):
    return value[0:5]

# ����Ҫ���������Ŀ��html��Ҫ����ϣ�
# {% load process %}
