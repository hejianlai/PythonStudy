import json
data = {'number':6,'name':'pythontab'}
jsonData = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'))
print(jsonData)