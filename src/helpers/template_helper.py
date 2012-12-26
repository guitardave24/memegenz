import os
import sys

#sys.path.append(os.path.abspath('../mako'))

from mako.template import Template
from mako.lookup import TemplateLookup

lookup = TemplateLookup(directories=['templates'])

def render(template_name, **kwargs):
  template = lookup.get_template(template_name)
  if not template:
    return None
  return template.render(**kwargs)
