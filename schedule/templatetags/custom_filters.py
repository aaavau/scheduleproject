from django import template

register = template.Library()

@register.filter
def uppercase(value):
    """文字列を大文字に変換"""
    return value.upper()
