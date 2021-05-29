from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = "Renames a Django Project"

    def add_arrguments(self, parser):
        parser.add_argument('new_project_name', type=str, help="Please provide the name of the django p[roject needs to change")

    def handler(self,*args, **kwargs):
        new_project_name = kwargs['new_project_name']

        files_to_rename = ['boilerplate/settings/base.py','boilerplate/wsgi.py', 'manage.py']
        folder_name = 'boilerplate'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace(new_project_name)

            with open(f,'w') as file:
                file.write(filedata)

        os.rename(folder_name, new_project_name)

    
        self.stdout.write(self.style.SUCCESS("Succefully renamed the project to provided name {} ".format(new_project_name)))