# Generated by Django 5.0.6 on 2024-06-25 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sabpaisa_app', '0037_alter_transactiondetail_trans_complete_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactiondetail',
            name='pg_name',
            field=models.CharField(default='NA', max_length=255, null=True),
        ),
    ]
