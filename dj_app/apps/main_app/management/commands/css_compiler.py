"""
Needs for apps 'lable' property be assigned in each app.py
"""
from django.core.management.base import BaseCommand
from django.apps import apps
from django.conf import settings
import os
import sass


class Command(BaseCommand):
    help = 'Compiling css'

    def handle(self, *args, **options):
        for i in apps.get_app_configs():
            try:
                self.stdout.write('Compiling css files for {app}...'.format(app=i.label))

                sass.compile(
                    dirname=(
                        os.path.join(settings.BASE_DIR, 'sass/{folder}'.format(folder=i.label)),
                        os.path.join(settings.BASE_DIR, 'statics/{folder}/css'.format(folder=i.label)),
                    ),
                    output_style='compressed'
                )
            except Exception as exc:
                self.stderr.write(self.style.ERROR(exc))
                continue

            self.stdout.write(self.style.SUCCESS('Compiling complete'))
