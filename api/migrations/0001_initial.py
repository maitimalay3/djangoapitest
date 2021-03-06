# Generated by Django 3.2.2 on 2021-05-16 08:37

from django.db import migrations, models
import utils.uuid_helper


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LongRunningTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lrtid', models.CharField(default=utils.uuid_helper.generate_lrtid, max_length=100, unique=True)),
                ('state', models.IntegerField(choices=[(1, 'Processing'), (2, 'Complete'), (3, 'Failed')], default=1)),
                ('result', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Long Running Tasks',
            },
        ),
    ]
