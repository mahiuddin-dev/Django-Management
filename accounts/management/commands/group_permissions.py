
from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
import logging

from project import models
from accounts.models import UserProfile

GROUPS_PERMISSIONS = {
    'managers': {
        models.Project: ['add', 'change', 'delete', 'view'],
        UserProfile: ['add', 'change', 'delete', 'view'],
    },
    'workers': {
        models.Project: ['view'],
    }
}

GROUPS = {
    "managers": {
        "group": ["add", "delete", "change", "view"],
        "user": ["add", "delete", "change", "view"]
    }
}


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    help = "Create default groups"

    def handle(self, *args, **options):
        # Loop groups
        for group_name in GROUPS_PERMISSIONS:
            # Get or create group
            group, created = Group.objects.get_or_create(name=group_name)
            # Loop models in group
            for model_cls in GROUPS_PERMISSIONS[group_name]:
                # Loop permissions in group/model
                for perm_index, perm_name in \
                        enumerate(GROUPS_PERMISSIONS[group_name][model_cls]):
                    # Generate permission name as Django would generate it
                    codename = perm_name + "_" + model_cls._meta.model_name
                    try:
                        # Find permission object and add to group
                        perm = Permission.objects.get(codename=codename)
                        group.permissions.add(perm)
                        self.stdout.write("Adding " + codename + " to group " + group.__str__())
                    except Permission.DoesNotExist:
                        self.stdout.write(codename + " not found")

        for group_name in GROUPS:

            new_group, created = Group.objects.get_or_create(name=group_name)

            # Loop models in group
            for app_model in GROUPS[group_name]:

                # Loop permissions in group/model
                for permission_name in GROUPS[group_name][app_model]:

                    # Generate permission name as Django would generate it
                    name = "Can {} {}".format(permission_name, app_model)
                    print("Creating {}".format(name))

                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning("Permission not found with name '{}'.".format(name))
                        continue

                    new_group.permissions.add(model_add_perm)
