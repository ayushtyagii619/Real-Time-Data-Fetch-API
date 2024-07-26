# Generated by Django 5.0.6 on 2024-06-25 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('txn_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('act_amount', models.FloatField(blank=True, null=True)),
                ('pg_name', models.CharField(default='NA', max_length=255)),
                ('pg_pay_mode', models.CharField(default='NA', max_length=255)),
                ('pg_response_code', models.CharField(default='NA', max_length=255)),
                ('pg_return_amount', models.FloatField(blank=True, null=True)),
                ('pg_txn_id', models.CharField(default='NA', max_length=255)),
                ('alert_flag', models.CharField(default='NA', max_length=255)),
                ('amount_type', models.CharField(default='NA', max_length=255)),
                ('application_fail_url', models.CharField(default='NA', max_length=255)),
                ('application_succ_url', models.CharField(default='NA', max_length=255)),
                ('auth_code', models.CharField(default='NA', max_length=255)),
                ('bank_txn_id', models.CharField(default='NA', max_length=255)),
                ('challan_no', models.CharField(default='NA', max_length=255)),
                ('changed_on_followup', models.CharField(default='NA', max_length=255)),
                ('client_id', models.IntegerField(blank=True, null=True)),
                ('client_name', models.CharField(default='NA', max_length=255)),
                ('client_request_ip', models.CharField(default='NA', max_length=255)),
                ('convcharges', models.FloatField(blank=True, null=True)),
                ('ep_charges', models.FloatField(blank=True, null=True)),
                ('enquiry_counter', models.IntegerField(default=0)),
                ('enquiry_date', models.DateTimeField(blank=True, null=True)),
                ('gst', models.FloatField(blank=True, null=True)),
                ('mapping_id', models.IntegerField(blank=True, null=True)),
                ('paid_amount', models.FloatField(blank=True, null=True)),
                ('payee_amount', models.FloatField(blank=True, null=True)),
                ('payee_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('payee_first_name', models.CharField(default='NA', max_length=255)),
                ('payee_lst_name', models.CharField(default='NA', max_length=255)),
                ('payee_mid_name', models.CharField(default='NA', max_length=255)),
                ('payee_mob', models.CharField(default='NA', max_length=255)),
                ('payment_mode', models.CharField(default='NA', max_length=255)),
                ('program_id', models.CharField(default='NA', max_length=255)),
                ('refund_date', models.CharField(blank=True, max_length=255, null=True)),
                ('refund_message', models.CharField(default='NA', max_length=255)),
                ('refund_status_code', models.CharField(default='NA', max_length=255)),
                ('reg_number', models.CharField(default='NA', max_length=255)),
                ('resp_msg', models.CharField(default='NA', max_length=255)),
                ('sabpaisa_resp_code', models.CharField(default='NA', max_length=255)),
                ('status', models.CharField(default='NA', max_length=255)),
                ('trans_complete_date', models.DateTimeField(auto_now_add=True)),
                ('trans_date', models.DateTimeField(auto_now_add=True)),
                ('client_code', models.CharField(blank=True, max_length=255, null=True)),
                ('client_txn_id', models.CharField(blank=True, max_length=255, null=True)),
                ('uit_application_id', models.CharField(default='NA', max_length=255)),
                ('vpa', models.CharField(default='NA', max_length=255)),
                ('vpa_remarks', models.CharField(default='NA', max_length=255)),
                ('is_settled', models.BooleanField(default=False)),
                ('pag_response_code', models.CharField(default='NA', max_length=255)),
                ('charge_back_amount', models.FloatField(blank=True, null=True)),
                ('charge_back_date', models.DateTimeField(blank=True, null=True)),
                ('charge_back_status', models.CharField(default='NA', max_length=255)),
                ('settlement_date', models.DateTimeField(blank=True, null=True)),
                ('settlement_amount', models.FloatField(blank=True, null=True)),
                ('channel_id', models.CharField(default='NA', max_length=255)),
                ('bankTxnId', models.CharField(default='NA', max_length=255)),
                ('broser_name', models.CharField(blank=True, max_length=255, null=True)),
                ('trans_push_date', models.DateTimeField(blank=True, null=True)),
                ('trans_flag', models.BooleanField(default=False)),
                ('udf20', models.CharField(default='NA', max_length=255)),
                ('donation_amount', models.FloatField(default=0)),
                ('card_brand', models.CharField(default='NA', max_length=255)),
                ('device_name', models.CharField(default='NA', max_length=10)),
                ('bank_message', models.CharField(default='NA', max_length=255)),
                ('fee_forward', models.CharField(default='NA', max_length=5)),
                ('payer_confirmation', models.BooleanField(default=False)),
                ('refunded_date', models.DateTimeField(blank=True, null=True)),
                ('settlement_status', models.CharField(default='NA', max_length=100)),
                ('settlement_by', models.CharField(default='NA', max_length=150)),
                ('settlement_bank_ref', models.CharField(blank=True, max_length=150, null=True)),
                ('settlement_remarks', models.CharField(default='NA', max_length=150)),
                ('settlement_utr', models.CharField(default='NA', max_length=150)),
                ('sent_notification_payer_confirmation_dt', models.DateTimeField(blank=True, null=True)),
                ('sent_notification_payer_confirmation_url', models.CharField(default='NA', max_length=500)),
                ('payer_confirmation_respones', models.CharField(default='NA', max_length=50)),
                ('payer_confirmation_respones_dt', models.DateTimeField(blank=True, null=True)),
                ('payer_confirmation_request_ct', models.IntegerField(blank=True, null=True)),
                ('refund_request_from', models.CharField(default='NA', max_length=150)),
                ('chargeback_request_from', models.CharField(default='NA', max_length=150)),
                ('gst_rate_type', models.CharField(default='NA', max_length=10)),
                ('udf19', models.CharField(default='NA', max_length=255)),
                ('ep_conv_rate', models.FloatField(blank=True, null=True)),
                ('gst_rate', models.FloatField(blank=True, null=True)),
                ('sp_conv_rate', models.FloatField(blank=True, null=True)),
                ('ep_conv_rate_type', models.CharField(default='NA', max_length=10)),
                ('sp_conv_rate_type', models.CharField(default='NA', max_length=10)),
                ('bank_errorcode', models.CharField(default='NA', max_length=255)),
                ('sabpaisa_errorcode', models.CharField(default='NA', max_length=255)),
                ('settlement_bank_amount', models.FloatField(blank=True, null=True)),
                ('settlement_bank_amount_date', models.DateTimeField(blank=True, null=True)),
                ('terminal_status', models.CharField(blank=True, max_length=50, null=True)),
                ('is_charge_back', models.BooleanField(default=False)),
                ('charge_back_debit_amount', models.FloatField(default=0)),
                ('charge_back_credit_date_to_merchant', models.DateTimeField(blank=True, null=True)),
                ('charge_back_remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
