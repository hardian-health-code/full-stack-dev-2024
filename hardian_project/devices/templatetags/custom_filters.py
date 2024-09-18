from django import template

register = template.Library()

@register.filter
def get_attr(dictionary, key):
    return dictionary.get(key, None)

@register.filter
def snake_to_title(value):
    if not isinstance(value, str):
        return value
    return value.replace('_', ' ').title()
