# Generated by Django 3.0.3 on 2020-04-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycustomer', '0020_delete_homeloan'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeLoan',
            fields=[
                ('loan_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=30)),
                ('Email', models.CharField(default='', max_length=40)),
                ('Gender', models.CharField(default='', max_length=10)),
                ('Graduate', models.CharField(default='', max_length=10)),
                ('Married', models.CharField(default='', max_length=10)),
                ('Number', models.IntegerField(default=0)),
                ('Employ', models.CharField(default='', max_length=10)),
                ('Income', models.IntegerField(default=0)),
                ('Loan', models.IntegerField(default=0)),
                ('Area', models.CharField(default='', max_length=10)),
                ('Status', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
