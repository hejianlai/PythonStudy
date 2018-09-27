from django.shortcuts import render,HttpResponse
from app01 import models

from django import forms
from django.forms import fields as Ffields
from django.forms import widgets as Fwidgets
class UserInfoModelForm(forms.ModelForm):

    is_rmb = Ffields.CharField(widget=Fwidgets.CheckboxInput())

    class Meta:
        model = models.UserInfo
        fields = '__all__'
        # fields =  ['username','email']
        # exclude = ['username']
        labels = {
            'username': '用户名',
            'email': '邮箱',
        }
        help_texts = {
            'username': '...'
        }
        widgets = {
            'username': Fwidgets.Textarea(attrs={'class': 'c1'})
        }
        error_messages = {
            '__all__':{

            },
            'email': {
                'required': '邮箱不能为空',
                'invalid': '邮箱格式错误..',
            }
        }
        field_classes = {
            # 'email': Ffields.URLField
        }

        # localized_fields=('ctime',)

    def clean_username(self):
        old = self.cleaned_data['username']
        return old

class UserInfoForm(forms.Form):
    username = Ffields.CharField(max_length=32)
    email = Ffields.EmailField()
    user_type = Ffields.ChoiceField(
        choices=models.UserType.objects.values_list('id','caption')
    )

    def __init__(self, *args, **kwargs):
        super(UserInfoForm,self).__init__(*args, **kwargs)
        self.fields['user_type'].choices = models.UserType.objects.values_list('id','caption')


def index(request):
    if request.method == "GET":
        obj = UserInfoModelForm()
        return render(request,'index.html',{'obj': obj})
    elif request.method == "POST":
        obj = UserInfoModelForm(request.POST)
        if obj.is_valid():
            # obj.save()
            instance = obj.save(False)
            instance.save()
            obj.save_m2m()


        # print(obj.is_valid())
        # print(obj.cleaned_data)
        # print(obj.errors.as_json())
        return render(request,'index.html',{'obj': obj})


def user_list(request):
    li = models.UserInfo.objects.all().select_related('user_type')
    return render(request,'user_list.html',{'li': li})

def user_edit(request, nid):
    # 获取当前id对象的用户信息
    # 显示用户已经存在数据
    if request.method == "GET":
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(instance=user_obj)
        return render(request,'user_edit.html',{'mf': mf, 'nid': nid})
    elif request.method == 'POST':
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(request.POST,instance=user_obj)
        if mf.is_valid():

            mf.save()
        else:
            print(mf.errors.as_json())
        return render(request,'user_edit.html',{'mf': mf, 'nid': nid})




def ajax(request):
    return render(request, 'ajax.html')

def ajax_json(request):
    import time
    time.sleep(3)
    print(request.POST)
    ret = {'code': True , 'data': request.POST.get('username')}
    import json
    return HttpResponse(json.dumps(ret))

def upload(request):
    return render(request,'upload.html')

def upload_file(request):
    username = request.POST.get('username')
    fafafa = request.FILES.get('fafafa')
    import os
    img_path = os.path.join('static/imgs/',fafafa.name)
    with open(img_path,'wb') as f:
        for item in fafafa.chunks():
            f.write(item)

    ret = {'code': True , 'data': img_path}
    import json
    return HttpResponse(json.dumps(ret))

def kind(request):
    return render(request, 'kind.html')

def upload_img(request):
    request.GET.get('dir')
    print(request.FILES.get('fafafa'))
    # 获取文件保存
    import json
    dic = {
        'error': 0,
        'url': '/static/imgs/20130809170025.png',
        'message': '错误了...'
    }

    return HttpResponse(json.dumps(dic))
import os
import time
import json
def file_manager(request):
    """
    文件管理
    :param request:
    :return:
    {
        moveup_dir_path:
        current_dir_path:
        current_url:
        file_list: [
            {
                'is_dir': True,
                'has_file': True,
                'filesize': 0,
                'dir_path': '',
                'is_photo': False,
                'filetype': '',
                'filename': xxx.png,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            },
            {
                'is_dir': True,
                'has_file': True,
                'filesize': 0,
                'dir_path': '',
                'is_photo': False,
                'filetype': '',
                'filename': xxx.png,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }
        ]

    }


    """
    dic = {}
    root_path = 'C:/Users/Administrator/PycharmProjects/day24/static/'
    static_root_path = '/static/'
    request_path = request.GET.get('path')
    if request_path:
        abs_current_dir_path = os.path.join(root_path, request_path)
        move_up_dir_path = os.path.dirname(request_path.rstrip('/'))
        dic['moveup_dir_path'] = move_up_dir_path + '/' if move_up_dir_path else move_up_dir_path

    else:
        abs_current_dir_path = root_path
        dic['moveup_dir_path'] = ''

    dic['current_dir_path'] = request_path
    dic['current_url'] = os.path.join(static_root_path, request_path)

    file_list = []
    for item in os.listdir(abs_current_dir_path):
        abs_item_path = os.path.join(abs_current_dir_path, item)
        a, exts = os.path.splitext(item)
        is_dir = os.path.isdir(abs_item_path)
        if is_dir:
            temp = {
                'is_dir': True,
                'has_file': True,
                'filesize': 0,
                'dir_path': '',
                'is_photo': False,
                'filetype': '',
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }
        else:
            temp = {
                'is_dir': False,
                'has_file': False,
                'filesize': os.stat(abs_item_path).st_size,
                'dir_path': '',
                'is_photo': True if exts.lower() in ['.jpg', '.png', '.jpeg'] else False,
                'filetype': exts.lower().strip('.'),
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }

        file_list.append(temp)
    dic['file_list'] = file_list
    return HttpResponse(json.dumps(dic))

