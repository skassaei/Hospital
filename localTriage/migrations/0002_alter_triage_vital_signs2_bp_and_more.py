# Generated by Django 4.1.7 on 2023-02-24 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localTriage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triage',
            name='vital_Signs2_BP',
            field=models.CharField(max_length=200, null=True, verbose_name='vital_Signs2_BP'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='vital_Signs2_RP',
            field=models.CharField(max_length=200, null=True, verbose_name='vital_Signs2_RP'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='vital_Signs2_RR',
            field=models.CharField(max_length=200, null=True, verbose_name='vital_Signs2_RR'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='vital_Signs2_Spo2',
            field=models.CharField(max_length=200, null=True, verbose_name='vital_Signs2_Spo2'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='vital_Signs2_T',
            field=models.CharField(max_length=200, null=True, verbose_name='vital_Signs2_T'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='vital_Signs3_BP',
            field=models.CharField(max_length=200, null=True, verbose_name='vital_Signs3_BP'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='vital_Signs3_RP',
            field=models.CharField(max_length=200, null=True, verbose_name='vital_Signs3_RP'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='vital_Signs3_RR',
            field=models.CharField(max_length=200, null=True, verbose_name='vital_Signs3_RR'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='vital_Signs3_Spo2',
            field=models.CharField(max_length=200, null=True, verbose_name='vital_Signs3_Spo2'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='vital_Signs3_T',
            field=models.CharField(max_length=200, null=True, verbose_name='vital_Signs3_T'),
        ),
    ]
