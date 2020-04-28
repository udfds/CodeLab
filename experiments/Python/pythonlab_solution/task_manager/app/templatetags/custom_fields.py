from django import template

register = template.Library()


@register.filter(name='addClass')
def addClass(value, args):
    return value.as_widget(attrs={'class': args})