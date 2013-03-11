import os
from django.core.exceptions import ImproperlyConfigured

def env_variable(variable):
  try:
    return os.environ[variable]
  except KeyError:
    message = "Environmental variable %s is unset" % variable
    raise ImproperlyConfigured(message)