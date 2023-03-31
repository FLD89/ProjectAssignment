from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def get_engineer_name(context, engineer_id):
    engineers = context['engineers']
    for engineer in engineers:
        if engineer.engineer_id == engineer_id:
            return str(engineer.engineer_name)

