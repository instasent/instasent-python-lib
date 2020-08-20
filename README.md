Welcome to __Instasent Python SDK__. This repository contains Python SDK for Instasent's REST API.

# Notice!

> **Verify** product is currently deprecated and will be removed in the next release. The same functionality can be easily implemented by sending an SMS. If you need help migrating please contact usage

## Installation

The easiest way to install the SDK is either via pip:

```
$ pip install instasent
```

or manually by downloading the source and run the setup.py script:

```
$ python setup.py install
```

# Usage

Check the [examples directory](https://github.com/instasent/instasent-python-lib/tree/master/examples) to see working examples of this SDK usage

### Sending an SMS

```python
import instasent

client = instasent.Client('my-token')
response = client.send_sms('Company', '+34666666666', 'test message')

print response['response_code']
print response['response_body']
```

If you want to send an Unicode SMS (i.e with 😀 emoji) you only need to replace `send_sms` call to `send_sms_unicode`

```python
response = client.send_sms_unicode('Company', '+34666666666', 'Unicode test: ña éáíóú 😀')
```

## Available actions

```
SMS
instasent.send_sms(sender, to, text)
instasent.send_sms_unicode(sender, to, text)
instasent.get_sms(page, per_page)
instasent.get_sms_by_id(message_id)

LOOKUP
instasent.do_lookup(to)
instasent.get_lookup_by_id(id)
instasent.get_lookups(page, per_page)

ACCOUNT
instasent.get_account_balance()
```

# Full documentation

Full documentation of the API can be found at http://docs.instasent.com/

# Getting help

If you need help installing or using the SDK, please contact Instasent Support at support@instasent.com

If you've instead found a bug in the library or have a feature request, go ahead and open an issue or pull request!
