# Generated by Django 3.0.3 on 2020-04-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycustomer', '0005_auto_20200402_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates',
            name='upload_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]