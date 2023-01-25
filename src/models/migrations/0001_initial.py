# Generated by Django 4.1.3 on 2023-01-25 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(choices=[('ISRC', 'ISRC'), ('ICPN', 'ICPN'), ('GRid', 'GRid'), ('ProprietaryId', 'ProprietaryId')], default='ICPN', max_length=100)),
                ('id_value', models.CharField(default='A0', max_length=100, unique=True)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_choice', models.CharField(choices=[('Single', 'Single'), ('Album', 'Album')], max_length=8)),
                ('release_type', models.CharField(choices=[('BookletFrontImageRelease', 'BookletFrontImageRelease'), ('DigitalBoxSetRelease', 'DigitalBoxSetRelease'), ('LyricSheetRelease', 'LyricSheetRelease'), ('Playlist', 'Playlist'), ('StemBundle', 'StemBundle'), ('NonMusicalWorkBasedGameRelease', 'NonMusicalWorkBasedGameRelease'), ('ClassicalAlbum', 'ClassicalAlbum'), ('Season', 'Season'), ('WallPaperRelease', 'WallPaperRelease'), ('AlertToneRelease', 'AlertToneRelease'), ('Series', 'Series'), ('SingleResourceRelease', 'SingleResourceRelease'), ('UserDefined', 'UserDefined'), ('RingtoneRelease', 'RingtoneRelease'), ('EBookRelease', 'EBookRelease'), ('RingbackToneRelease', 'RingbackToneRelease'), ('Album', 'Album'), ('VideoMastertoneRelease', 'VideoMastertoneRelease'), ('AudioBookRelease', 'AudioBookRelease'), ('BookletBackImageRelease', 'BookletBackImageRelease'), ('DramaticoMusicalVideoRelease', 'DramaticoMusicalVideoRelease'), ('LongFormNonMusicalWorkVideoRelease', 'LongFormNonMusicalWorkVideoRelease'), ('VideoAlbum', 'VideoAlbum'), ('Documentary', 'Documentary'), ('DjMix', 'DjMix'), ('ShortFilm', 'ShortFilm'), ('Drama', 'Drama'), ('SheetMusicRelease', 'SheetMusicRelease'), ('MultimediaSingle', 'MultimediaSingle'), ('MultimediaAlbum', 'MultimediaAlbum'), ('MultimediaDigitalBoxedSet', 'MultimediaDigitalBoxedSet'), ('ClassicalMultimediaAlbum', 'ClassicalMultimediaAlbum'), ('AudioDramaRelease', 'AudioDramaRelease'), ('VideoSingle', 'VideoSingle'), ('BookletRelease', 'BookletRelease'), ('AsPerContract', 'AsPerContract'), ('Bundle', 'Bundle'), ('ConcertVideo', 'ConcertVideo'), ('BackCoverImageRelease', 'BackCoverImageRelease'), ('Single', 'Single'), ('MusicalWorkBasedGameRelease', 'MusicalWorkBasedGameRelease'), ('ClassicalDigitalBoxedSet', 'ClassicalDigitalBoxedSet')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(choices=[('ISRC', 'ISRC'), ('ICPN', 'ICPN'), ('GRid', 'GRid'), ('ProprietaryId', 'ProprietaryId')], max_length=100)),
                ('id_value', models.CharField(default='S0', max_length=150, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('audio_file', models.FileField(upload_to='resources/')),
                ('has_crbt', models.BooleanField()),
                ('crbt_start_time', models.CharField(blank=True, max_length=10)),
                ('crbt_code', models.CharField(blank=True, max_length=50)),
                ('has_clip', models.BooleanField()),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.album')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.order')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_type', models.CharField(default='Artist', max_length=250)),
                ('role', models.CharField(choices=[('Artist', 'Artist'), ('Contributor', 'Contributor')], default='MainArtist', max_length=150)),
                ('name', models.CharField(max_length=250)),
                ('song', models.ManyToManyField(to='models.song')),
            ],
            options={
                'verbose_name_plural': 'Parties',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(choices=[('ISRC', 'ISRC'), ('ICPN', 'ICPN'), ('GRid', 'GRid'), ('ProprietaryId', 'ProprietaryId')], default='ProprietaryId', max_length=100)),
                ('id_value', models.CharField(default='I0', max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('image_file', models.FileField(upload_to='resources/')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.song')),
            ],
        ),
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(upload_to='resources/')),
                ('name', models.CharField(max_length=100)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.song')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.order'),
        ),
    ]
