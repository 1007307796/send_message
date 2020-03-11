import zhenzismsclient as smsclient
from weather import get_text

text = get_text()
#print(text)
client = smsclient.ZhenziSmsClient(
    'https://sms_developer.zhenzikj.com',
    'yourid',
    'yourkey')

params = {'message':text, 'number':'receive_number'}
result = client.send(params)
print(result)
