# Generated by Django 3.0.3 on 2020-04-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycustomer', '0006_updates_upload_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='Upload_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='updates',
            name='valid_upto',
            field=models.DateField(blank=True, null=True),
        ),
    ]
