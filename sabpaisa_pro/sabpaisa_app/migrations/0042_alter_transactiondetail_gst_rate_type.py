# Generated by Django 5.0.6 on 2024-06-25 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sabpaisa_app', '0041_alter_transactiondetail_fee_forward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactiondetail',
            name='gst_rate_type',
            field=models.CharField(default='NA', max_length=10, null=True),
        ),
    ]
