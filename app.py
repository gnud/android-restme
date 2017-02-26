#!/usr/bin/env python
 
import os
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
 
def create_index_html():
    model_name = "Greetings"

    item1={"access_mod": "public", "type": "String", "name": "first_name"}
    item2={"access_mod": "public", "type": "String", "name": "middle_name"}
    item3={"access_mod": "public", "type": "String", "name": "last_name"}
    create_model(model_name, [item1, item2, item3])

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
        html = render_template('task.java', context)
        f.write(html)
 
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
        html = render_template("model.java", context)
        f.write(html)
 
 
def main():
    create_index_html()
 
########################################
 
if __name__ == "__main__":
    main()