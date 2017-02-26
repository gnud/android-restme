#!/usr/bin/env python
 
import os
import json
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


package_name = 'com.myrest.rest'
output_path = 'output/rest/'


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
 

def create_task(model_name, model_items):
    """Renders a task based on the java asynctask template"""

    create_model(model_name, model_items)

    task_class_name = "%sCallTask" % model_name.title()
    fname = "%s%s.java" % (output_path, task_class_name)
    
    representation_model = model_name
    
    context = {
        'package': package_name,
        'task_class_name': task_class_name,
        'representationModel': representation_model,
        'restUri': 'http://somerest.org/api/'
    }
    #
    with open(fname, 'w') as f:
        rendered_code = render_template('task.java', context)
        f.write(rendered_code)
 

def create_model(model_name, fields):
    fname = "%s%s.java" % (output_path, model_name)
    tname = "%s.java" % model_name
    
    representation_model = model_name

    context = {
        'package': package_name,
        'representationModel': representation_model,
        'fields': fields
    }
    #
    with open(fname, 'w') as f:
        rendered_code = render_template("model.java", context)
        f.write(rendered_code)
 

def process_model(model_path):
    with open(model_path) as data_file:
        try:
            model_name = os.path.splitext(os.path.basename(model_path))[0].title()
        except Exception:
            print('Processing of %s failed.' % model_name)

        model_items = json.load(data_file)

        # Hardcoded mode
        create_task(model_name, model_items)


def main():
    # ensure the output directory is ready
    try:
        os.mkdir(output_path)
    except Exception:
        pass

    process_model("data/greetings.json")
 
########################################
 
if __name__ == "__main__":
    main()
