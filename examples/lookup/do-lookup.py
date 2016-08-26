import instasent

client = instasent.Client('my-token')
response = client.do_lookup('+34666666666')

print response['response_code']
print response['response_body']