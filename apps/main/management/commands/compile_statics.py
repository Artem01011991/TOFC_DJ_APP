"""
App 'label' property must be assigned in each apps.py
"""
import os

import sass
from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Compiling css'

    def add_arguments(self, parser):
        parser.add_argument('app_names', nargs='*')  # For adding folder name as command prompt argument

    def handle(self, *args, **options):
        configs = (apps.get_app_config(i) for i in options['app_names']) \
            if options['app_names'] else apps.get_app_configs()

        for config in configs:
            try:
                # CSS compiling
                self.stdout.write('Compiling CSS files for {app}...'.format(app=config.label))
                sass.compile(
                    dirname=(
                        os.path.join(settings.BASE_DIR, 'build/{folder}/sass'.format(folder=config.label)),
                        os.path.join(
                            settings.BASE_DIR,
                            settings.STATIC_ROOT,
                            '{folder}/css'.format(folder=config.label)
                        ),
                    ),
                    output_style='compressed',
                )

                # HTML compiling
                self.stdout.write('Compiling HTML files for {app}...'.format(app=config.label))

            except Exception as exc:
                self.stderr.write(self.style.ERROR(exc))
                continue

            self.stdout.write(self.style.SUCCESS('Compiling complete'))
