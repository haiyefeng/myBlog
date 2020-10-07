from __future__ import absolute_import

import json
import datetime

from django.conf import settings


def blue_settings(request):
    try:
        if request.user.is_anonymous:
            username = ''
        else:
            username = request.user.username

        context = {
            'APP_CODE': settings.APP_CODE,
            # 本地静态文件访问
            'STATIC_URL': settings.STATIC_URL,
            # 当前页面，主要为了login_required做跳转用
            'APP_PATH': request.get_full_path(),
            # URL前缀
            'SITE_URL': settings.SITE_URL,
            # 静态资源版本号,用于指示浏览器更新缓存
            'STATIC_VERSION': settings.STATIC_VERSION,
            # 用户名
            'USERNAME': username,
            # 是否调试模式
            'DEBUG': json.dumps(settings.DEBUG),
            # 当前时间
            'NOW': datetime.datetime.now(),
            # 前后端联合开发的静态资源路径, 这个变量可选配置
            'BK_STATIC_URL': settings.STATIC_URL.rstrip('/'),
            # 是否使用blueking_language切换国际化语言
            'IS_DISPLAY_LANGUAGE_CHANGE': settings.IS_DISPLAY_LANGUAGE_CHANGE
        }
    except Exception:
        raise
    return context
