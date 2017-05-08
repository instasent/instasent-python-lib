import instasent

client = instasent.Client('my-token')
response = client.send_sms_unicode('My company', '+34666666666', 'test message áéíóú')

print response['response_code']
print response['response_body']