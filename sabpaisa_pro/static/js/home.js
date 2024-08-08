document.getElementById('fetchDataButton').addEventListener('click', function() {
    document.getElementById('tokenInputContainer').style.display = 'block';
});

document.getElementById('submitTokenButton').

addEventListener('click', function() {
    const token = document.getElementById('jwtToken').value;

    fetch('transaction/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
        const transactionDataDiv = document.getElementById('transactionData');
        let html = '<table class="table table-bordered"><thead><tr>';
        
        // Define friendly column names
        const columnNames = {
            txn_id: 'Transaction ID',
            act_amount: 'Actual Amount',
            pg_name: 'Payment Gateway Name',
            pg_pay_mode: 'Payment Gateway Mode',
            pg_response_code: 'Payment Gateway Response Code',
            pg_return_amount: 'Payment Gateway Return Amount',
            pg_txn_id: 'Payment Gateway Transaction ID',
            alert_flag: 'Alert Flag',
            amount_type: 'Amount Type',
            application_fail_url: 'Application Fail URL',
            application_succ_url: 'Application Success URL',
            auth_code: 'Authorization Code',
            bank_txn_id: 'Bank Transaction ID',
            challan_no: 'Challan Number',
            changed_on_followup: 'Changed on Followup',
            client_id: 'Client ID',
            client_name: 'Client Name',
            client_request_ip: 'Client Request IP',
            convcharges: 'Convenience Charges',
            ep_charges: 'EP Charges',
            enquiry_counter: 'Enquiry Counter',
            enquiry_date: 'Enquiry Date',
            gst: 'GST',
            mapping_id: 'Mapping ID',
            paid_amount: 'Paid Amount',
            payee_amount: 'Payee Amount',
            payee_email: 'Payee Email',
            payee_first_name: 'Payee First Name',
            payee_lst_name: 'Payee Last Name',
            payee_mid_name: 'Payee Middle Name',
            payee_mob: 'Payee Mobile',
            payment_mode: 'Payment Mode',
            program_id: 'Program ID',
            refund_date: 'Refund Date',
            refund_message: 'Refund Message',
            refund_status_code: 'Refund Status Code',
            reg_number: 'Registration Number',
            resp_msg: 'Response Message',
            sabpaisa_resp_code: 'SabPaisa Response Code',
            status: 'Status',
            trans_complete_date: 'Transaction Complete Date',
            trans_date: 'Transaction Date',
            client_code: 'Client Code',
            client_txn_id: 'Client Transaction ID',
            uit_application_id: 'UIT Application ID',
            vpa: 'Virtual Payment Address',
            vpa_remarks: 'Virtual Payment Address Remarks',
            is_settled: 'Is Settled',
            pag_response_code: 'Payment Gateway Response Code',
            charge_back_amount: 'Chargeback Amount',
            charge_back_date: 'Chargeback Date',
            charge_back_status: 'Chargeback Status',
            settlement_date: 'Settlement Date',
            settlement_amount: 'Settlement Amount',
            channel_id: 'Channel ID',
            bankTxnId: 'Bank Transaction ID',
            broser_name: 'Browser Name',
            trans_push_date: 'Transaction Push Date',
            trans_flag: 'Transaction Flag',
            udf20: 'User Defined Field 20',
            donation_amount: 'Donation Amount',
            card_brand: 'Card Brand',
            device_name: 'Device Name',
            bank_message: 'Bank Message',
            fee_forward: 'Fee Forward',
            payer_confirmation: 'Payer Confirmation',
            refunded_date: 'Refunded Date',
            settlement_status: 'Settlement Status',
            settlement_by: 'Settlement By',
            settlement_bank_ref: 'Settlement Bank Reference',
            settlement_remarks: 'Settlement Remarks',
            settlement_utr: 'Settlement UTR',
            sent_notification_payer_confirmation_dt: 'Sent Notification Payer Confirmation Date',
            sent_notification_payer_confirmation_url: 'Sent Notification Payer Confirmation URL',
            payer_confirmation_respones: 'Payer Confirmation Response',
            payer_confirmation_respones_dt: 'Payer Confirmation Response Date',
            payer_confirmation_request_ct: 'Payer Confirmation Request Count',
            refund_request_from: 'Refund Request From',
            chargeback_request_from: 'Chargeback Request From',
            gst_rate_type: 'GST Rate Type',
            udf19: 'User Defined Field 19',
            ep_conv_rate: 'EP Conversion Rate',
            gst_rate: 'GST Rate',
            sp_conv_rate: 'SP Conversion Rate',
            ep_conv_rate_type: 'EP Conversion Rate Type',
            sp_conv_rate_type: 'SP Conversion Rate Type',
            bank_errorcode: 'Bank Error Code',
            sabpaisa_errorcode: 'SabPaisa Error Code',
            settlement_bank_amount: 'Settlement Bank Amount',
            settlement_bank_amount_date: 'Settlement Bank Amount Date',
            retry_payment_reponse_code: 'Retry Payment Response Code',
            retry_payment_reponse_msg: 'Retry Payment Response Message',
            retry_payment_date: 'Retry Payment Date',
            refund_amount: 'Refund Amount',
            refund_reponse_code: 'Refund Response Code',
            refund_reponse_msg: 'Refund Response Message',
            refund_date1: 'Refund Date 1',
            refund_date2: 'Refund Date 2',
            refunded_amount1: 'Refunded Amount 1',
            refunded_amount2: 'Refunded Amount 2',
            refund_amount1: 'Refund Amount 1',
            refund_amount2: 'Refund Amount 2',
            refund_requested: 'Refund Requested',
            charge_back_amount1: 'Chargeback Amount 1',
            charge_back_amount2: 'Chargeback Amount 2',
            charge_back_date1: 'Chargeback Date 1',
            charge_back_date2: 'Chargeback Date 2',
            charge_back_remarks1: 'Chargeback Remarks 1',
            charge_back_remarks2: 'Chargeback Remarks 2',
            charge_back_settlement_amount1: 'Chargeback Settlement Amount 1',
            charge_back_settlement_amount2: 'Chargeback Settlement Amount 2',
            is_flagged: 'Is Flagged',
            ewallet_settled: 'Ewallet Settled',
            file_upload_dt: 'File Upload Date',
            resp_code: 'Response Code',
            txn_status: 'Transaction Status'
        };

        // Assuming all objects have the same keys, get the first object keys for headers
        if (data.length > 0) {
            Object.keys(data[0]).forEach(key => {
                html += `<th>${columnNames[key] || key}</th>`;
            });
            html += '</tr></thead><tbody>';
            
            data.forEach(transaction => {
                html += '<tr>';
                Object.values(transaction).forEach(value => {
                    html += `<td>${value}</td>`;
                });
                html += '</tr>';
            });
            
            html += '</tbody></table>';
        } else {
            html = '<p>No transactions found.</p>';
        }

        transactionDataDiv.innerHTML = html;
    })
    .catch(error => console.error('Error fetching transaction data:', error));
});
