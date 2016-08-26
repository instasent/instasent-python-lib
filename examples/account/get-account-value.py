import instasent

client = instasent.Client('my-token')
response = client.get_account_balance()

print response['response_code']
print response['response_body']