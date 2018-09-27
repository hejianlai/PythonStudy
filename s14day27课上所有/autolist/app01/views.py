from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from app01 import models
import json
class BaseResponse(object):
    def __init__(self):
        self.status = True
        self.data = None
        self.message = None

class ServerView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'server.html')


class ServerJsonView(View):
    def get(self,request,*args, **kwargs):
        response = BaseResponse()
        try:
            # 获取要显示的列
            # 获取数据
            table_config = [
                {
                    'q': 'id',
                    'title': '主机名',
                    'display':0,
                    'text': {},
                    'attr': {}
                },
                {
                    'q': 'hostname',
                    'title': '主机名',
                    'display':1,
                    'text': {'content': '{m}','kwargs': {'m':'@hostname'}},
                    'attr': {'orginal':'@hostname','k2':'v2'}
                },
                # '{n}-{m}'.format({'n': 'hostname','m':'@hostname'}) => hostname-c1.com
                {
                    'q': 'port',
                    'title': '端口',
                    'display':1,
                    'text': {'content': '{m}','kwargs': {'m':'@port'}},
                    'attr': {'k1':'@port','k2':'v2'}
                },
                {
                    'q': 'business_unit_id',
                    'title': '业务线ID',
                    'display':1,
                    # 去全局变量business_unit_list = [
                    #      {id:1,name:'WEB'},
                    #      {id:2,name:'存储'},
                    #      {id:3,name:'商城'},
                    # ]
                    'text': {'content': '{m}','kwargs': {'m':'@@business_unit_list'}},
                    'attr': {'k1':'@business_unit_id','k2':'v2'}
                },
                {
                    'q': 'business_unit__name',
                    'title': '业务线名称',
                    'display':1,
                    'text': {'content': '{key}-{m}','kwargs': {'key': '@business_unit_id','m':'@business_unit__name'}},
                    'attr': {'k1':'@business_unit__name','k2':'v2'}
                },
                {
                    'q': None,
                    'title': '操作',
                    'display':1,
                    'text': {'content': '<a href="/server-detail-{m}.html">查看详细</a>','kwargs': {'m':'@id'}},
                    'attr': {'k1':'@id','k2':'v2'}
                }
            ]

            values_list = []
            for item in table_config:
                if item['q']:
                    values_list.append(item['q'])

            data_list = models.Server.objects.values(*values_list)
            # [{},{}]
            data_list = list(data_list)
            print(data_list)
            response.data = {
                'table_config': table_config,
                'data_list': data_list,
            }
        except Exception as e:
            response.status = False
            response.message = str(e)
        return HttpResponse(json.dumps(response.__dict__))



class BusinessView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'business.html')


class BusinessJsonView(View):
    def get(self,request,*args, **kwargs):
        response = BaseResponse()
        try:
            # 获取要显示的列
            # 获取数据
            table_config = [
                {
                    'q': 'id',
                    'title': 'Id',
                    'display':1,
                },
                {
                    'q': 'name',
                    'title': '业务线名称',
                    'display':1,
                },
                {
                    'q': None,
                    'title': '操作',
                    'display':1,
                }
            ]

            values_list = []
            for item in table_config:
                if item['q']:
                    values_list.append(item['q'])

            data_list = models.BusinessUnit.objects.values(*values_list)
            # [{},{}]
            data_list = list(data_list)
            response.data = {
                'table_config': table_config,
                'data_list': data_list,
            }
        except Exception as e:
            response.status = False
            response.message = str(e)
        return HttpResponse(json.dumps(response.__dict__))
