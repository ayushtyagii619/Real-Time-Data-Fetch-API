# Generated by Django 5.0.6 on 2024-06-25 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sabpaisa_app', '0004_alter_transactiondetail_refund_status_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactiondetail',
            name='vpa',
            field=models.CharField(default='NA', max_length=255, null=True),
        ),
    ]
