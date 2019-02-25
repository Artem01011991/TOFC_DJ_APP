from django.conf import settings
from django.contrib.sites.models import Site
from django.db import migrations


def site_domen(apps, schema_editor):
    host_name = settings.ALLOWED_HOSTS[settings.SITE_ID - 1]
    Site.objects.create(id=settings.SITE_ID, domain=host_name, name=host_name)


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('auth', '0001_initial')
    ]

    operations = [
        migrations.RunPython(site_domen)
    ]
