# Generated by Django 3.1 on 2020-10-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_draw_prizeid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=10)),
            ],
        ),
    ]
