# Generated by Django 2.1.4 on 2018-12-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_game_description_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
