# Generated by Django 5.0.1 on 2024-02-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0006_alter_package_package_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='package_type',
            field=models.CharField(max_length=10),
        ),
    ]
