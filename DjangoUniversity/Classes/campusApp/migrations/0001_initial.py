# Generated by Django 4.1.1 on 2022-09-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(blank=True, default='', max_length=60)),
                ('campus_id', models.IntegerField(blank=True, default='')),
                ('state', models.CharField(blank=True, default='', max_length=60)),
            ],
            options={
                'verbose_name_plural': 'University Campus',
            },
        ),
    ]
