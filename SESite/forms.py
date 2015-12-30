# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from SESite.models import Person
__author__ = 'andyyang'
USER_TYPE = ((1,'教师'),(2,'学生'),(3,'助教'))
class PersonUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label="密码")
    class Meta:
        model = User
        fields = ('username','email','password')

class PersonProfile(forms.ModelForm):
    type  = forms.ChoiceField(required=True,widget=forms.RadioSelect,choices=USER_TYPE,label="身份")
    idnum = forms.CharField(label="学号/教工号")
    class Meta:
        model = Person
        fields = ('idnum','type')

class CourseMaterialsForm(forms.Form):
    docfile = forms.FileField(
        label='请选择文件'
    )
class HomeworkForm(forms.Form):
    docfile = forms.FileField(
        label='请选择文件,请勿超过100M'
    )
