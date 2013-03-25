from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'mtax',
    'HOST': 'localhost'
  }
}

INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

DEBUG_TOOLBAR_PANELS = (
  'debug_toolbar.panels.version.VersionDebugPanel',
  'debug_toolbar.panels.timer.TimerDebugPanel',
  'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
  'debug_toolbar.panels.headers.HeaderDebugPanel',
  'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
  'debug_toolbar.panels.template.TemplateDebugPanel',
  'debug_toolbar.panels.sql.SQLDebugPanel',
  'debug_toolbar.panels.signals.SignalDebugPanel',
  'debug_toolbar.panels.logger.LoggingPanel',
)

def custom_show_toolbar(request):
  return True  # Always show toolbar, for example purposes only.

DEBUG_TOOLBAR_CONFIG = {
  'INTERCEPT_REDIRECTS': False,
  'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
  'HIDE_DJANGO_SQL': False,
  'TAG': 'body',
  'ENABLE_STACKTRACES' : True,
}
