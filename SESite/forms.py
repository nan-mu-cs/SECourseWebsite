# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from SESite.models import Person
__author__ = 'andyyang'
USER_TYPE = ((1,'Teacher'),(2,'Student'))
class PersonUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput());
    class Meta:
        model = User
        fields = ('username','email','password')

class PersonProfile(forms.ModelForm):
    type  = forms.ChoiceField(required=True,widget=forms.RadioSelect,choices=USER_TYPE)
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
