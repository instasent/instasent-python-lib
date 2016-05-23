import instasent

client = instasent.Client('my-token')
response = client.send_sms('My company', '+34666666666', 'test message')

print response['response_code']
print response['response_body']