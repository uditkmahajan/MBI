# Generated by Django 3.0.3 on 2020-04-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycustomer', '0015_auto_20200404_1541'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.AddField(
            model_name='mycustomer',
            name='Feedback',
            field=models.TextField(default='', max_length=300),
        ),
    ]
