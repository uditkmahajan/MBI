# Generated by Django 3.0.3 on 2020-04-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycustomer', '0013_auto_20200403_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='Profile',
            field=models.ImageField(default='', upload_to='feedback'),
        ),
    ]
