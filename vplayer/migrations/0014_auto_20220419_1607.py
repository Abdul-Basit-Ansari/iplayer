# Generated by Django 3.2.8 on 2022-04-19 11:07

from django.db import migrations, models
import vplayer.models


class Migration(migrations.Migration):

    dependencies = [
        ('vplayer', '0013_auto_20220419_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maudio',
            name='cover',
            field=models.ImageField(default=1, upload_to='mycover', validators=[vplayer.models.validate_file_extension]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mvideo',
            name='cover',
            field=models.ImageField(blank=True, default='', null=True, upload_to='videoscover', validators=[vplayer.models.validate_file_extension]),
        ),
    ]
