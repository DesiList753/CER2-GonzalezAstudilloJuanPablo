# Generated by Django 4.2.5 on 2023-10-22 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usmweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='tipo',
            field=models.CharField(choices=[('S', 'SUSPENSION ACTIVIDADES'), ('C', 'SUSPENSION CLASE'), ('T', 'Informacion')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='usmweb/img/logo_entidad/'),
        ),
    ]
