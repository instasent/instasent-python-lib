import instasent

client = instasent.Client('my-token')
response = client.get_sms_by_id('id')

print response['response_code']
print response['response_body']
