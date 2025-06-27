import re
from django import template

register = template.Library()

@register.filter
def extract_parenthesis(value):
    """ดึงข้อความในวงเล็บ เช่น 'เทคโนโลยีสารสนเทศ ( IT )' => 'IT' """
    match = re.search(r'\((.*?)\)', value)
    return match.group(1).strip() if match else value
