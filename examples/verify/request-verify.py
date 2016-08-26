import instasent

client = instasent.Client('my-token')
response = client.request_verify('My company', '+34666666666', 'Your code is %token%')

print response['response_code']
print response['response_body']