# Generated by Django 2.2.6 on 2019-10-30 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_slave'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='slave_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Slave'),
            preserve_default=False,
        ),
    ]