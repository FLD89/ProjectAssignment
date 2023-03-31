from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def get_assigned_engineers(context, proj_id):
    lookups = context['lookups']
    record = ""
    for lookup in lookups:
        if lookup.project_id_id == proj_id:
            if record:
                record += ", "
            record += lookup.engineer_id_id
    if record:
        return record
    else:
        return "(none)"


@register.simple_tag(takes_context=True)
def get_available_engineers(context, project_id):
    project = context['project']
    engineers = context['engineers']
    trainings = context['trainings']
    lookups = context['lookups']

    assigned_engineers = []
    for lookup in lookups:
        if lookup.project_id_id == project.project_id:
            assigned_engineers.append(lookup.engineer_id_id)

    trained_engineers = []
    for training in trainings:
        if training.software == project.software:
            trained_engineers.append(str(training.engineer_id_id))

    available_engineers = ""
    for trained_id in trained_engineers:
        if trained_id not in assigned_engineers:
            if available_engineers:
                available_engineers += ", "
            available_engineers += f"{trained_id} ({str(engineers.get(engineer_id=trained_id))})"
    if available_engineers:
        return available_engineers
    else:
        return "No unassigned Software Engineers with required Software Training"
