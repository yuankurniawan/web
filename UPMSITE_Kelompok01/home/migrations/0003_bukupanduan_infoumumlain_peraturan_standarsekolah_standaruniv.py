# Generated by Django 3.0.8 on 2020-10-25 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_akreditasiprodi_akreditasiumum_auditprodi_auditumum_folderutama_informasiumum'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandarUniv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('nama_folder', models.CharField(default='', max_length=256)),
                ('desc_folder', models.TextField(default='', max_length=256)),
                ('baseFolder_nama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.FolderUtama')),
                ('prodi_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.listProdi')),
            ],
        ),
        migrations.CreateModel(
            name='StandarSekolah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('nama_folder', models.CharField(default='', max_length=256)),
                ('desc_folder', models.TextField(default='', max_length=256)),
                ('baseFolder_nama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.FolderUtama')),
                ('prodi_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.listProdi')),
            ],
        ),
        migrations.CreateModel(
            name='Peraturan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('nama_folder', models.CharField(default='', max_length=256)),
                ('desc_folder', models.TextField(default='', max_length=256)),
                ('baseFolder_nama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.FolderUtama')),
                ('prodi_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.listProdi')),
            ],
        ),
        migrations.CreateModel(
            name='InfoUmumLain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('nama_folder', models.CharField(default='', max_length=256)),
                ('desc_folder', models.TextField(default='', max_length=256)),
                ('baseFolder_nama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.FolderUtama')),
                ('prodi_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.listProdi')),
            ],
        ),
        migrations.CreateModel(
            name='BukuPanduan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('nama_folder', models.CharField(default='', max_length=256)),
                ('desc_folder', models.TextField(default='', max_length=256)),
                ('baseFolder_nama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.FolderUtama')),
                ('prodi_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.listProdi')),
            ],
        ),
    ]
