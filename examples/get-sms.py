import instasent

client = instasent.Client('my-token')
response = client.get_sms(1, 50)

print response['response_code']
print response['response_body']

