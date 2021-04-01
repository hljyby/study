from django import template

register = template.Library()


@register.filter(name='test')
def test(value,arg):
    return value + arg
