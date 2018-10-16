"""
Needs for apps 'lable' property be assigned in each app.py
"""
from django.apps import apps
import sass


if __name__ == '__main__':
    for i in apps.get_app_configs():
        try:
            sass.compile(
                dirname=('sass/{folder}'.format(folder=i.lable), '../statics/{folder}/css'.format(folder=i.lable)),
                output_style='compressed')
        except:
            continue
