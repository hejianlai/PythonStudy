from django.shortcuts import render
import requests
# pip3 install requests
# Create your views here.


def req(request):
    response = requests.get('http://weatherapi.market.xiaomi.com/wtr-v2/weather?cityId=101121301')
    #print(response.content) # 字节
    response.encoding = 'utf-8'
    #print(response.text)    # 字符串
    return render(request, 'req.html',{'result': response.text})
