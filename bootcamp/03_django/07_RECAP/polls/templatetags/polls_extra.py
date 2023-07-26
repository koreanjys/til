# polls/
#   templatetags/
#       __init__.py
#      *polls_extra.py

from django import template

register = template.Library()

@register.simple_tag
def check_user_voted(reply, user):
    return reply.is_voted(user)