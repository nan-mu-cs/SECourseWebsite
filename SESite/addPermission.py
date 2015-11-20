from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

__author__ = 'andyyang'
from SESite import views

def addPermission():
    content_type = ContentType.objects.get(app_label="SESite",model="person")
    teacher_group = Group.objects.get(name="Teacher")
    #teacher_group.permissions.remove()
    can_teach = Permission.objects.create(name="Can teach",codename="can_teach",content_type=content_type)
    can_post_NoticeMessage = Permission.objects.create(name="Can post notice message",codename="can_post_NoticeMessage",
                                                   content_type=content_type)
    teacher_group.permissions = [can_teach,can_post_NoticeMessage,]
    #teacher_group.permissions.add(can_post_NoticeMessage)
    student_group = Group.objects.get(name="Student")
    can_study = Permission.objects.create(name="Can study",codename="can_study",content_type=content_type)
    #student_group.permissions.add(can_study)
    student_group.premissions = [can_study,]
