# Generated by Django 3.0.3 on 2020-04-02 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycustomer', '0004_mycustomer_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycustomer',
            name='Time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mycustomer',
            name='last_seen',
            field=models.DateField(blank=True, null=True),
        ),
    ]