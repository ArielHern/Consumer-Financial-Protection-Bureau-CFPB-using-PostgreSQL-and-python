from CRUD import run_command


# command = '''
# CREATE VIEW bank_account_wo_complaints AS
#     SELECT * FROM bank_account_complaints
#     WHERE consumer_complaint_narrative IS
#  NULL;
# '''
# run_command(command)

# command = '''
# CREATE VIEW credit_card_wo_complaints as
#     SELECT * FROM credit_card_complaints
#     WHERE consumer_complaint_narrative IS NULL;
# '''
# run_command(command)

# command = '''
# CREATE VIEW bank_account_w_complaints AS
#     SELECT * FROM bank_account_complaints
#     WHERE consumer_complaint_narrative IS NOT
#  NULL;
# '''
# run_command(command)

# command = '''
# CREATE VIEW bank_account_wo_complaints AS
#     SELECT * FROM bank_account_complaints
#     WHERE consumer_complaint_narrative IS
#  NULL;
# '''
# run_command(command)

'''
create two  views w/ complaints and w/out complaints
'''

# command = '''
# CREATE VIEW with_complaints AS
#     SELECT * from credit_card_w_complaints
#     UNION ALL
#     SELECT * from bank_account_w_complaints;
# '''
# run_command(command)
# command = '''
# CREATE VIEW without_complaints AS
#     SELECT * FROM credit_card_wo_complaints
#     UNION ALL
#     SELECT * FROM bank_account_wo_complaints;
# '''
# run_command(command)
# print('Views create')


'''
view for well's fargo where customer did not dispute
their response
'''
command = '''
CREATE VIEW wells_complaints_v AS (
    SELECT CAST(complaint_id AS int) AS complaint_id,
           date_received, product, sub_product, issue, company,
           state, zip_code, submitted_via, date_sent,
           company_response_to_consumer,
           timely_response, consumer_disputed
    FROM bank_account_complaints
     WHERE state = 'CA'
           AND consumer_disputed = 'No'
          AND company = 'Wells Fargo & Company')'''
run_command(command)
print('View created')
