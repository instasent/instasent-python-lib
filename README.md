Welcome to __Instasent Python SDK__. This repository contains Instasent's Python SDK and samples for REST API.

## Installation

The easiest way to install the instasent package is either via pip:

```
$ pip install instasent
```

or manually by downloading the source and run the setup.py script:

```
$ python setup.py install
```

## Example
### Send an SMS
You can check 'examples/send-sms.py' file.
```python

import instasent

client = instasent.Client('my-token')
response = client.send_sms('Mi company', '+34666666666', 'test message')

print response['response_code']
print response['response_body']

```
## Available functions
```
SMS
instasent.send_sms(sender, to, text)
instasent.get_sms(page, per_page)
instasent.get_sms_by_id(message_id)

VERIFY
instasent.request_verify(sender, to, text); // text must include %token% string
instasent.check_verify(id, token)
instasent.get_verify_by_id(id)
instasent.get_verify()

LOOKUP
instasent.do_lookup(to)
instasent.get_lookup_by_id(id)
instasent.get_lookups(page, per_page)

ACCOUNT
instasent.get_account_balance()

```
## Documentation
Complete documentation at :
[http://docs.instasent.com/](http://docs.instasent.com/).

# Getting help

If you need help installing or using the library, please contact Instasent Support at support@instasent.com first.
If you've instead found a bug in the library or would like new features added, go ahead and open issues or pull requests against this repo!