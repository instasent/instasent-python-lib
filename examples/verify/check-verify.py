import instasent

client = instasent.Client('my-token')
response = client.check_verify('id', 'token')

print response['response_code']
print response['response_body']