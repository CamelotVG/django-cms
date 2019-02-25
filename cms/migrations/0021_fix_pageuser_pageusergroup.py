# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
from ._base import IrreversibleMigration


class Migration(migrations.Migration):
    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
    ]
    operations = [
        migrations.AddField(
            model_name='PageUser',
            name='cms_created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='created_users', on_delete=models.CASCADE, null=True, blank=True),
        ),
        migrations.RenameField(
            model_name='PageUserGroup',
            old_name='created_by',
            new_name='cms_created_by',
        ),
    ]
