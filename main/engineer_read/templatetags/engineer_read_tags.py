from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def get_training_record(context, engineer_id):
    trainings = context['trainings']
    record = ""
    for training in trainings:
        if training.engineer_id_id == engineer_id:
            if record:
                record += ", "
            record += training.software
    if record:
        return record
    else:
        return "None"


