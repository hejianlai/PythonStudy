
from django import forms
from crm import models
from django.utils.translation import pgettext, ugettext as _
#
# class CustomerModelForm(forms.ModelForm):
#     class Meta:
#         model = models.Customer
#         fields = "__all__"






def CreateModelForm(request,admin_obj):

    class Meta:
        model = admin_obj.model
        # if admin_obj.readonly_fields:
        #     exclude = admin_obj.readonly_fields
        #else:
        fields = "__all__"

    def __new__(cls, *args, **kwargs):
        #print("base fields",cls.base_fields)
        for field_name,field_obj in cls.base_fields.items():
            #print(field_name,dir(field_obj))
            field_obj.widget.attrs['class'] = 'form-control'
            # field_obj.widget.attrs['maxlength'] = getattr(field_obj,'max_length' ) if hasattr(field_obj,'max_length') \
            #     else ""
            if field_name in admin_obj.readonly_fields:
                field_obj.widget.attrs['disabled'] = True


        return forms.ModelForm.__new__(cls)


    def default_clean(self):
        #print("default clean:",self)
        for field in admin_obj.readonly_fields:
            print("readonly",field,self.instance)
            field_val_from_db  = getattr(self.instance,field)
            field_val = self.cleaned_data.get(field)
            if field_val_from_db == field_val:
                print("field not change ")
            else: # 被篡改了
                self.add_error(field,' "%s" is a readonly field ,value should be "%s" '% (field, field_val_from_db))

        print("cleaned data:",self.cleaned_data)


    dynamic_model_form = type("DynamicModelForm",(forms.ModelForm,), {"Meta":Meta})
    setattr(dynamic_model_form,"__new__",__new__)
    setattr(dynamic_model_form,"clean",default_clean)
    return dynamic_model_form