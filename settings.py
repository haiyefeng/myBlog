import os

PAAS_V2_ENVIRONMENT = os.environ.get('BK_ENV', 'development')
ENVIRONMENT = {
    'development': 'dev',
    'testing': 'stag',
    'production': 'prod',
}.get(PAAS_V2_ENVIRONMENT)

DJANGO_CONF_MODULE = 'config.{env}'.format(env=ENVIRONMENT)

try:
    _module = __import__(DJANGO_CONF_MODULE, globals(), locals(), ['*'])
except ImportError as e:
    raise ImportError("Could not import config '%s' (Is it on sys.path?): %s"
                      % (DJANGO_CONF_MODULE, e))

for _setting in dir(_module):
    if _setting == _setting.upper():
        locals()[_setting] = getattr(_module, _setting)
