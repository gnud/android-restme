#!/usr/bin/env python

import os
import json
from jinja2 import Environment, FileSystemLoader
import sys


class RestApp(object):
    """
    Application to build and deploy an Android rest API package.
    """

    def __init__(self):
        # Setup Jinja 2 templates engine
        app_root = os.path.dirname(os.path.abspath(__file__))
        self.template_environment = Environment(
                autoescape=False,
                loader=FileSystemLoader(os.path.join(app_root, 'templates')),
                trim_blocks=False)

        # Defining fields
        self.app_name = ''
        self.rest_uri = ''
        self.package_name = ''
        self.model_name = ''
        self.deploy_path = ''
        self.model_items = ''

    def render_template(self, template_filename, context):
        """ JINJA2 helper method
        :param template_filename:
        :param context:
        :return: str The rendered template
        """
        return self.template_environment.get_template(template_filename).render(context)

    def create_task(self):
        """Renders a task based on the java AsyncTask template"""

        self.create_model()
        static_name = 'CallTask'
        template_name = 'task.java'

        task_class_name = '%s%s' % (self.model_name.title(), static_name)
        fname = os.path.join(self.deploy_path, '%s.java' % task_class_name)

        context = {
            'package': self.package_name,
            'task_class_name': task_class_name,
            'representationModel': self.model_name,
            'restUri': self.rest_uri
        }

        with open(fname, 'w') as f:
            rendered_code = self.render_template(template_name, context)
            f.write(rendered_code)

    def create_model(self):
        template_name = 'model.java'
        fname = os.path.join(self.deploy_path, '%s.java' % self.model_name.title())

        context = {
            'package': self.package_name,
            'representationModel': self.model_name,
            'fields': self.model_items
        }

        with open(fname, 'w') as f:
            rendered_code = self.render_template(template_name, context)
            f.write(rendered_code)

    def process_project(self, project_path, full_project_path):
        """
        Parses the restproject.json as JSON and the builds the REST API
        :param str project_path: Working path (CWD) of the project
        :param str full_project_path: The full path of the project JSON file
        """
        with open(full_project_path) as data_file:
            data = json.load(data_file)

            # extract data
            self.app_name = data['app_name']
            self.rest_uri = data['server']
            self.package_name = data['package_name']
            self.model_name = data['model_name']
            self.deploy_path = os.path.join(project_path, data['deploy_path'],
                                            self.package_name.replace('.', os.path.sep))
            self.model_items = data['fields']

            # ensure the output directory is ready
            try:
                os.mkdir(self.deploy_path)
            except OSError:
                print('Deploy path exists "%s".' % self.deploy_path)
                print('continuing anyways ...')

            # Hardcoded mode
            self.create_task()


def main():
    project_path = sys.argv[1] if len(sys.argv) > 1 else ''

    if not os.path.isdir(project_path):
        print('Locating project failed for "%s".' % project_path)
        return

    full_project_path = os.path.join(project_path, 'restproject.json')
    RestApp().process_project(project_path, full_project_path)


########################################

if __name__ == '__main__':
    main()
