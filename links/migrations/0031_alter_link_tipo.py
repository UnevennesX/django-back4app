# Generated by Django 5.1 on 2024-08-24 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0030_alter_backuplog_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='tipo',
            field=models.CharField(choices=[('Samplicious', 'Samplicious'), ('Spectrum', 'Spectrum'), ('Cint', 'Cint'), ('Progede', 'Progede'), ('Sample-cube', 'Sample-cube'), ('Invite', 'Invite'), ('Internos', 'Internos'), ('Roirocket', 'Roirocket')], default='Samplicious', max_length=50),
        ),
    ]
