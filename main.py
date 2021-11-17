from jinja2 import FileSystemLoader, Environment
import json
import sys

file_system_loader = FileSystemLoader(searchpath='./')
env = Environment(
    loader=file_system_loader,
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True,
    auto_reload=False,
)

# Load parameters for the template
parameters_file = sys.argv[0]
with open(parameters_file, "r") as dag_spec:
    template_parameters = json.load(dag_spec)

# Render template
template_file = sys.argv[1]
template = env.get_template(template_file)
output_text = template.render(template_parameters)

print(output_text)

output_file_name = template_parameters['output_file_name']
with open(output_file_name, "w") as result_file:
    result_file.write(output_text)

print("COMPLETE")
