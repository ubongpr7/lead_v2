# Generated by Django 4.2.16 on 2025-01-17 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidoe_text', '0007_textfile_trimmed_video_textfile_video_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='textfile',
            name='timestamp_end',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='textfile',
            name='timestamp_start',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='lead_maker/audio_files'),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='bg_music_text',
            field=models.FileField(blank=True, null=True, upload_to='lead_maker/background_txt/'),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='generated_blank_video',
            field=models.FileField(blank=True, null=True, upload_to='lead_maker/generated_blank_video/'),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='generated_final_bgm_video',
            field=models.FileField(blank=True, null=True, upload_to='lead_maker/generated_bgm_video/'),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='generated_final_bgmw_video',
            field=models.FileField(blank=True, null=True, upload_to='lead_maker/generated_bgmw_video/'),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='generated_final_video',
            field=models.FileField(blank=True, null=True, upload_to='lead_maker/generated_final_video/'),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='generated_srt',
            field=models.FileField(blank=True, null=True, upload_to='lead_maker/generated_srt/'),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='generated_subclips_srt',
            field=models.FileField(blank=True, null=True, upload_to='lead_maker/generated_subclips_srt/'),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='generated_watermarked_video',
            field=models.FileField(blank=True, null=True, upload_to='lead_maker/generated_watermarked_video/'),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='subclips_text_file',
            field=models.FileField(blank=True, null=True, upload_to='lead_maker/subclips_text_files/'),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='subtitle_file',
            field=models.FileField(blank=True, null=True, upload_to='lead_maker/subtitles/'),
        ),
    ]
