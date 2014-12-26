# -*- coding: utf-8 -*-

from appconf import AppConf

from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _


class DjangoCMSLayoutConf(AppConf):
    pass

    class Meta:
        prefix = 'djangocms_layout'