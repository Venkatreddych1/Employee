# Generated by Django 2.1.5 on 2020-07-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0002_auto_20200703_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_num',
            field=models.IntegerField(max_length=5, null=True),
        ),
    ]