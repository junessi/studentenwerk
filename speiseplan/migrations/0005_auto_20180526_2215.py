# Generated by Django 2.0.1 on 2018-05-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speiseplan', '0004_auto_20180525_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catering',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]