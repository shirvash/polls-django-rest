# Generated by Django 2.2.10 on 2021-10-06 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0005_auto_20211006_0227'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Complete',
            new_name='Reply',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='date_complete',
            new_name='date_reply',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='complete',
        ),
        migrations.AlterField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Poll'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Question'),
        ),
    ]