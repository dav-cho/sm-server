# Generated by Django 3.2.4 on 2021-06-13 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_auto_20210613_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='accounts.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reaction',
            name='author',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='accounts.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reaction',
            name='post',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='api.post'),
            preserve_default=False,
        ),
    ]
