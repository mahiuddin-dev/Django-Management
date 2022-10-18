
def user_groups_processor(request):
    groups = []
    user = request.user
    if user.is_authenticated:
        groups = list(user.groups.values_list('name', flat=True))
    return {'groups': groups}
