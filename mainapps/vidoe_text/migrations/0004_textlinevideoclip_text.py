# Generated by Django 4.2.16 on 2024-12-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidoe_text', '0003_textfile_trimmed_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='textlinevideoclip',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
