"""
App 'lable' property must be assigned in each app.py
"""
from django.core.management.base import BaseCommand
from django.apps import apps
from django.conf import settings
from dj_app.apps.main_app.settings import CSS_CLASS_NAMES
import os
import sass


class Command(BaseCommand):
    help = 'Compiling css'

    def add_arguments(self, parser):
        parser.add_argument('app_names', nargs='*')

    def handle(self, *args, **options):
        configs = (apps.get_app_config(i) for i in options['app_names']) if options['app_names'] else apps.get_app_configs()

        for i in configs:
            try:
                self.stdout.write('Compiling css files for {app}...'.format(app=i.label))
                sass.compile(
                    dirname=(
                        os.path.join(settings.BASE_DIR, 'sass/{folder}'.format(folder=i.label)),
                        os.path.join(settings.BASE_DIR, 'statics/{folder}/css'.format(folder=i.label)),
                    ),
                    output_style='compressed',
                    custom_functions={
                        sass.SassFunction('get-class-name', ('$class-name-key',), self._get_css_class_name)
                    }
                )
            except Exception as exc:
                self.stderr.write(self.style.ERROR(exc))
                continue

            self.stdout.write(self.style.SUCCESS('Compiling complete'))

    @staticmethod
    def _get_css_class_name(class_name_key):
        return '.' + CSS_CLASS_NAMES[class_name_key]
