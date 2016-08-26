import instasent

client = instasent.Client('my-token')
response = client.get_lookups('id')

print response['response_code']
print response['response_body']