# Generated by Django 4.1.7 on 2023-02-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localTriage', '0007_alter_triage_admintion_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triage',
            name='admintion_time',
            field=models.TimeField(null=True, verbose_name='ساعت مراجعه'),
        ),
    ]
