# Generated by Django 3.1.2 on 2020-11-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201106_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barufile',
            name='upload_file',
            field=models.FileField(max_length=50, null=True, upload_to=''),
        ),
    ]
