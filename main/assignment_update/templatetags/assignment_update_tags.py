from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def get_engineer_name(context, engineer_id):
    engineers = context['engineers']
    for engineer in engineers:
        if engineer.engineer_id == engineer_id:
            return str(engineer.engineer_name)


@register.simple_tag(takes_context=True)
def get_project_name(context, project_id):
    projects = context['projects']
    for project in projects:
        if project.project_id == project_id:
            return str(project.project_name)


@register.simple_tag(takes_context=True)
def get_available_engineers(context):
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


@register.simple_tag(takes_context=True)
def get_available_projects(context):
    trainings = context['trainings']
    current_lookup = context['lookup']
    projects = context['projects']
    lookups = context['lookups']

    trained_software = []
    for training in trainings:
        if training.engineer_id_id == current_lookup.engineer_id_id:
            trained_software.append(str(training.software))

    available_projects = []
    for project in projects:
        if project.software in trained_software:
            available_projects.append(str(project.project_id))

    for lookup in lookups:
        if lookup.project_id_id in available_projects:
            if lookup.engineer_id_id == current_lookup.engineer_id_id:
                available_projects.remove(lookup.project_id_id)

    available_projects_string = ""
    for available_project in available_projects:
        if available_projects_string:
            available_projects_string += ", "
        available_projects_string += f"{available_project} ({str(projects.get(project_id=available_project))})"

    if available_projects_string:
        return available_projects_string
    else:
        return "No Projects available that match Engineer's Software Training or are not already assigned to this Engineer"










