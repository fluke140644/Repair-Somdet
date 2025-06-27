# yourapp/templatetags/status_color.py
from django import template

register = template.Library()

@register.filter
def get_status_color(status):
    return {
        'pending': 'warning',
        'in_progress': 'primary',
        'completed': 'success',
        'repairclaim': 'purple',
        'cancelled': 'danger',
    }.get(status, 'secondary')