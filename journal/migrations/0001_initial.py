# Generated by Django 4.2.2 on 2023-06-24 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_id', models.BigIntegerField(auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('content', djrichtextfield.models.RichTextField(max_length=15000)),
                ('date', models.DateField(auto_now=True)),
                ('public', models.BooleanField()),
                ('self_image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=80, scale=None, size=[200, None], upload_to='self_images/')),
                ('day_image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=80, scale=None, size=[600, None], upload_to='self_images/')),
                ('selected_theme', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]