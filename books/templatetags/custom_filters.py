from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def startswith(string, start):
    if string and start:
        return string.startswith(start)
    return False

@register.simple_tag
def modify_query(**kwargs):
    from django.http import QueryDict
    import urllib.parse
    
    query_dict = QueryDict(mutable=True)
    # Get current query parameters
    for key, value in kwargs.items():
        if value is not None:
            query_dict[key] = value
    
    return query_dict.urlencode()