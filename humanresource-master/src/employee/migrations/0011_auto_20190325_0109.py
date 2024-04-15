# Generated by Django 2.1.7 on 2019-03-25 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_auto_20190325_0107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emergency',
            options={'ordering': ['-created'], 'verbose_name': 'Emergency', 'verbose_name_plural': 'Emergency'},
        ),
        migrations.AddField(
            model_name='emergency',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created'),
        ),
        migrations.AddField(
            model_name='emergency',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated'),
        ),
    ]
