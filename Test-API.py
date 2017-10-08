import requests
r = requests.post('INVOKE_URL/STAGE/RESOURCE_NAME',
                  headers={'x-api-key': 'API KEY'},
                  json={'test':'test'})
print(r.text)