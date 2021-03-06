# Generated by Django 2.1.4 on 2018-12-21 17:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9 ]+$', 'Only lower case, upper case letters, numbers and spaces are allowed')])),
                ('description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9 ]+$', 'Only lower case, upper case letters, numbers and spaces are allowed')])),
                ('public', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaticResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9 ]+$', 'Only lower case, upper case letters, numbers and spaces are allowed')])),
                ('url', models.URLField()),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Game')),
            ],
        ),
    ]
