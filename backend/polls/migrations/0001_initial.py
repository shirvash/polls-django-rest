# Generated by Django 2.2.24 on 2021-12-04 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('date_end', models.DateTimeField()),
                ('description', models.TextField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reply', models.DateTimeField(auto_now_add=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, max_length=256)),
                ('type', models.CharField(choices=[('TEXT', 'TEXT'), ('CHOICE', 'CHOICE'), ('MULTICHOICE', 'MULTICHOICE')], default='TEXT', max_length=11)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(blank=True, max_length=255)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Poll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.Reply')),
            ],
        ),
    ]
