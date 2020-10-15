from django import template
register = template.Library()
'''自定义过滤器'''
@register.filter
def mutifiter(x,y):
    return x*y
@register.simple_tag
def mutitag(x,y):
    return x*y