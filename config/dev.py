from config.default import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
STATIC_URL = '/static/'
# Mysql configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认用mysql
        'NAME': 'my_blog',  # 数据库名 (默认与APP_ID相同)
        'USER': 'root',  # 你的数据库user
        'PASSWORD': '123456',  # 你的数据库password
        'HOST': '127.0.0.1',  # 开发的时候，使用localhost
        'PORT': 3307,  # 默认3306
    },
}
