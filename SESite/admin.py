#coding: utf-8
from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from pybb.models import Category, Forum, Topic, RenderableItem, Post, Profile, Attachment, TopicReadTrackerManager, \
    TopicReadTracker, ForumReadTrackerManager, ForumReadTracker, PollAnswerUser, PollAnswer
from SESite.models import Person, Class


class MyAdminSite(AdminSite):
    site_header = "教学辅助平台后台管理"
    site_title = "教学辅助平台后台管理"
    index_title = "教学辅助平台后台管理"

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Person)
admin_site.register(User)
admin_site.register(Category)
admin_site.register(Forum)
admin_site.register(Topic)
admin_site.register(Post)
admin_site.register(Profile)
admin_site.register(Attachment)
admin_site.register(TopicReadTracker)
admin_site.register(ForumReadTracker)
admin_site.register(PollAnswer)
admin_site.register(PollAnswerUser)
admin_site.register(Group)
admin_site.register(Class)
#admin.site.register(Person)
#sites.site = mysite