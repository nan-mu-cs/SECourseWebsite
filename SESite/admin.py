#coding: utf-8
from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from SESite.models import Person


class MyAdminSite(AdminSite):
    site_header = "教学辅助平台后台管理"
    site_title = "教学辅助平台后台管理"
    index_title = "教学辅助平台后台管理"

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Person)
admin_site.register(User)
#admin.site.register(Person)
#sites.site = mysite