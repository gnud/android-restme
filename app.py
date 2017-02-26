#!/usr/bin/env python
 
import os
import json
from jinja2 import Environment, FileSystemLoader
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
 

def create_task(deploy_path, model_name, model_items, rest_uri, package_name):
    """Renders a task based on the java asynctask template"""

    create_model(deploy_path, model_name, package_name, model_items)

    task_class_name = "%sCallTask" % model_name.title()
    fname = os.path.join(deploy_path, '%s.java' % task_class_name )

    representation_model = model_name
    
    context = {
        'package': package_name,
        'task_class_name': task_class_name,
        'representationModel': representation_model,
        'restUri': rest_uri
    }

    with open(fname, 'w') as f:
        rendered_code = render_template('task.java', context)
        f.write(rendered_code)
 

def create_model(deploy_path, model_name, package_name, fields):
    fname = os.path.join(deploy_path, '%s.java' % model_name )

    representation_model = model_name

    context = {
        'package': package_name,
        'representationModel': representation_model,
        'fields': fields
    }

    with open(fname, 'w') as f:
        rendered_code = render_template("model.java", context)
        f.write(rendered_code)
 

def process_model(project_path, model_path):
    with open(model_path) as data_file:
        try:
            model_name = os.path.splitext(os.path.basename(model_path))[0].title()
        except Exception:
            print('Processing of %s failed.' % model_name)

        data = json.load(data_file)

        # extract data
        app_name = data['app_name']
        rest_uri = data['server']
        package_name = data['package_name']
        model_name = data['model_name']
        deploy_path = os.path.join(project_path, data['deploy_path'], package_name.replace('.', os.path.sep), app_name)
        model_items = data['fields']

        # ensure the output directory is ready
        try:
            os.mkdir(deploy_path)
        except OSError:
            print('deploy_path exists "%s".' % deploy_path)
            print('continuing anyways ...')
            #return # TODO: make a question or sys argument that ask for overwrite
        except Exception as e:
            pass

        # Hardcoded mode
        create_task(deploy_path, model_name, model_items, rest_uri, package_name)


def main():
    project_path = sys.argv[1] if len(sys.argv) > 1 else ''

    if not os.path.isdir(project_path):
        print('Locating project failed for "%s".' % project_path)
        return

    full_project_path = os.path.join(project_path, 'restproject.json')

    process_model(project_path, full_project_path)
 
########################################
 
if __name__ == "__main__":
    main()
