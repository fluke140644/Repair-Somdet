from django import template

register = template.Library()

@register.filter
def duration_in_minutes(value):
    if not value:
        return "-"
    total_seconds = value.total_seconds()
    minutes = int(total_seconds // 60)
    hours = minutes // 60
    minutes = minutes % 60
    if hours > 0:
        return f"{hours}:{minutes}Hrs."
    else:
        return f"{minutes} min."