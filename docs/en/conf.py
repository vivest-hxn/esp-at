# -*- coding: utf-8 -*-
#
# English Language RTD & Sphinx config file
#
# Uses ../conf_common.py for most non-language-specific settings.

# Importing conf_common adds all the non-language-specific
# parts to this conf module
import sys
import os
import datetime

sys.path.insert(0, os.path.abspath('..'))
from conf_common import *  # noqa: F401, F403 - need to make available everything from common

current_year = datetime.datetime.now().year

# General information about the project.
project = u'ESP-AT User Guide'
copyright = u'2016 - {}, Espressif Systems (Shanghai) Co., Ltd.'.format(current_year)

pdf_title = u'ESP-AT User Guide'
# Final PDF filename will contains target and version
pdf_file_prefix = u'esp-at'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'
