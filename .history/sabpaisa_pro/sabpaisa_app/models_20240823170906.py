from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser , PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self,email,name,tc,password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not tc:
            raise ValueError('Please check the tc box')
        user = self.model(
            email = self.normalize_email(email),
            name=name,
            tc = tc,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,tc,password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class NewUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name='Email',max_length=200,unique=True)
    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','tc']
    

    def __str__(self):
        return self.email
    
      

class TransactionDetail(models.Model):
    txn_id = models.CharField(max_length=255, primary_key=True,null=False,default=False)
    act_amount = models.FloatField(null=True, blank=True)
    pg_name = models.CharField(max_length=255, default='NA',null=True)
    pg_pay_mode = models.CharField(max_length=255, default='NA',null=True)
    pg_response_code = models.CharField(max_length=255, default='NA',null=True)
    pg_return_amount = models.FloatField(null=True, blank=True)
    pg_txn_id = models.CharField(max_length=255, default='NA',null=True)
    alert_flag = models.CharField(max_length=255, default='NA',null=True)
    amount_type = models.CharField(max_length=255, default='NA')
    application_fail_url = models.CharField(max_length=255, default='NA')
    application_succ_url = models.CharField(max_length=255, default='NA')
    auth_code = models.CharField(max_length=255, default='NA',null=True)
    bank_txn_id = models.CharField(max_length=255, default='NA',null=True)
    challan_no = models.CharField(max_length=255, default='NA',null=True)
    changed_on_followup = models.CharField(max_length=255, default='NA')
    client_id = models.IntegerField(null=True, blank=True)
    client_name = models.CharField(max_length=255, default='NA',null=False)
    client_request_ip = models.CharField(max_length=255, default='NA')
    convcharges = models.FloatField(null=True, blank=True)
    ep_charges = models.FloatField(null=True, blank=True)
    enquiry_counter = models.IntegerField(default=0,null=True)
    enquiry_date = models.DateTimeField(null=True, blank=True)
    gst = models.FloatField(null=True, blank=True)
    mapping_id = models.IntegerField(null=True, blank=True)
    paid_amount = models.FloatField(null=True, blank=True)
    payee_amount = models.FloatField(null=True, blank=True)
    payee_email = models.EmailField(null=True, blank=True)
    payee_first_name = models.CharField(max_length=255, default='NA')
    payee_lst_name = models.CharField(max_length=255, default='NA')
    payee_mid_name = models.CharField(max_length=255, default='NA')
    payee_mob = models.CharField(max_length=255, default='NA')
    payment_mode = models.CharField(max_length=255, default='NA',null=True)
    program_id = models.CharField(max_length=255, default='NA')
    refund_date = models.CharField(max_length=255, null=True, blank=True)
    refund_message = models.CharField(max_length=255, default='NA',null=True)
    refund_status_code = models.CharField(max_length=255, default='NA',null=True)
    reg_number = models.CharField(max_length=255, default='NA')
    resp_msg = models.CharField(max_length=255, default='NA',null=True)
    sabpaisa_resp_code = models.CharField(max_length=255, default='NA')
    status = models.CharField(max_length=255, default='NA')
    trans_complete_date = models.DateTimeField(auto_now_add=True,null=True)
    trans_date = models.DateTimeField(auto_now_add=True)
    client_code = models.CharField(max_length=255, null=True, blank=True)
    client_txn_id = models.CharField(max_length=255, null=True, blank=True)
    uit_application_id = models.CharField(max_length=255, default='NA')
    vpa = models.CharField(max_length=255, default='NA',null=True)
    vpa_remarks = models.CharField(max_length=255, default='NA',null=True)
    is_settled = models.BooleanField(default=False,null=True)
    pag_response_code = models.CharField(max_length=255, default='NA')
    charge_back_amount = models.FloatField(null=True, blank=True)
    charge_back_date = models.DateTimeField(null=True, blank=True)
    charge_back_status = models.CharField(max_length=255, default='NA',null=True)
    settlement_date = models.DateTimeField(null=True, blank=True)
    settlement_amount = models.FloatField(null=True, blank=True)
    channel_id = models.CharField(max_length=255, default='NA')
    bankTxnId = models.CharField(max_length=255, default='NA')
    broser_name = models.CharField(max_length=255, null=True, blank=True)
    trans_push_date = models.DateTimeField(null=True, blank=True)
    trans_flag = models.BooleanField(default=False,null=True)
    udf20 = models.CharField(max_length=255, default='NA',null=True)
    donation_amount = models.FloatField(default=0,null=True)
    card_brand = models.CharField(max_length=255, default='NA',null=True)
    device_name = models.CharField(max_length=10, default='NA',null=True)
    bank_message = models.CharField(max_length=255, default='NA',null=True)
    fee_forward = models.CharField(max_length=5, default='NA',null=True)
    payer_confirmation = models.BooleanField(default=False,null=True)
    refunded_date = models.DateTimeField(null=True, blank=True)
    settlement_status = models.CharField(max_length=100, default='NA',null=True)
    settlement_by = models.CharField(max_length=150, default='NA',null=True)
    settlement_bank_ref = models.CharField(max_length=150, null=True, blank=True)
    settlement_remarks = models.CharField(max_length=150, default='NA',null=True)
    settlement_utr = models.CharField(max_length=150, default='NA',null=True)
    sent_notification_payer_confirmation_dt = models.DateTimeField(null=True, blank=True)
    sent_notification_payer_confirmation_url = models.CharField(max_length=500, default='NA',null=True)
    payer_confirmation_respones = models.CharField(max_length=50, default='NA',null=True)
    payer_confirmation_respones_dt = models.DateTimeField(null=True, blank=True)
    payer_confirmation_request_ct = models.IntegerField(null=True, blank=True)
    refund_request_from = models.CharField(max_length=150, default='NA',null=True)
    chargeback_request_from = models.CharField(max_length=150, default='NA',null=True)
    gst_rate_type = models.CharField(max_length=10, default='NA',null=True)
    udf19 = models.CharField(max_length=255, default='NA',null=True)
    ep_conv_rate = models.FloatField(null=True, blank=True)
    gst_rate = models.FloatField(null=True, blank=True)
    sp_conv_rate = models.FloatField(null=True, blank=True)
    ep_conv_rate_type = models.CharField(max_length=10, default='NA',null=True)
    sp_conv_rate_type = models.CharField(max_length=10, default='NA',null=True)
    bank_errorcode = models.CharField(max_length=255, default='NA',null=True)
    sabpaisa_errorcode = models.CharField(max_length=255, default='NA',null=True)
    settlement_bank_amount = models.FloatField(null=True, blank=True)
    settlement_bank_amount_date = models.DateTimeField(null=True, blank=True)
    terminal_status = models.CharField(max_length=50, null=True, blank=True)
    is_charge_back = models.BooleanField(default=False,null=True)
    charge_back_debit_amount = models.FloatField(default=0,null=True)
    charge_back_credit_date_to_merchant = models.DateTimeField(null=True, blank=True)
    charge_back_remarks = models.CharField(max_length=200, null=True, blank=True)
    bank_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.txn_id

# Create your models here.
