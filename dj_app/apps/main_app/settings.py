from django.conf import settings
import os
import json


with open(os.path.join(settings.BASE_DIR, 'jsons/element-ids.json')) as f:
    MAIN_PAGE_ELEMS_IDS = json.load(f)

CONFIG_NAME_BY_ID = {
            MAIN_PAGE_ELEMS_IDS['index']: 'index activation mode',
            MAIN_PAGE_ELEMS_IDS['binance']: 'binance activation mode',
            MAIN_PAGE_ELEMS_IDS['django']: 'django control'
        }
