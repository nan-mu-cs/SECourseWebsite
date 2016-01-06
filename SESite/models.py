# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Class(models.Model):
    #teacher = models.ForeignKey(User)
    class_time = models.CharField(max_length=128)
    classroom = models.CharField(max_length=128)
    class_name = models.CharField(max_length=128)
    class Meta:
        db_table = 'Class'
    def __unicode__(self):
        return self.class_name
class Person(models.Model):
    user = models.OneToOneField(User)
    idnum = models.CharField(max_length=20,primary_key=True)
    type = models.IntegerField()
    class Meta:
         db_table = 'Person'
    def __unicode__(self):
        return self.idnum
class Classmember(models.Model):
    class_info = models.ForeignKey(Class)
    member = models.ForeignKey(User)
class NoticeMessage(models.Model):
    writer = models.ForeignKey(User)
    message = models.CharField(max_length=2000)
    post_time = models.DateTimeField(auto_now_add=True)
    classid = models.IntegerField(default=1)
    class Meta:
        db_table = 'NoticeMessage'
    def __unicode__(self):
        return self.message

def coursematerials_upload_directory_path(instance,filename):
        return u'coursemeterials/user_{0}_{1}'.format(instance.user.username,filename)
class mCourseMaterials(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    upload_time = models.DateTimeField(auto_now_add=True)
    docfile = models.FileField(upload_to=coursematerials_upload_directory_path)
    classid = models.IntegerField(default=1)
    class Meta:
        db_table = 'CourseMaterials'
    def __unicode__(self):
        return self.docfile.name

class CourseIntro(models.Model):
    writer = models.ForeignKey(User)
    pre_intro = models.CharField(max_length=2000)
    materi_intro = models.CharField(max_length = 2000)
    score_consti = models.CharField(max_length = 2000) 
    post_time = models.DateTimeField(auto_now_add = True)
    classid = models.IntegerField(default=1)
    class Meta:
        db_table = 'CourseIntro'
    def __unicode__(self):
        return self.pre_intro

class TAIntro(models.Model):
    writer = models.ForeignKey(User)
    teacher_intro = models.CharField(max_length=2000)
    ta_intro = models.CharField(max_length = 2000)
    post_time = models.DateTimeField(auto_now_add = True)
    classid = models.IntegerField(default=1)
    class Meta:
        db_table = 'TAIntro'
    def __unicode__(self):
        return self.teacher_intro

class Homework(models.Model):
    assigner = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    post_time = models.DateTimeField(auto_now_add=True)
    due_time = models.DateTimeField(auto_now_add=False)
    classid = models.IntegerField(default=4)
    class Meta:
        db_table = 'Homework'
    def __unicode__(self):
        return self.description

def homework_upload_directory_path(instance,filename):
        return u'homework/user_{0}_{1}_{2}'.encode('utf-8').format(instance.student_ID_id,instance.homeworkid_id,filename)

class StudentHomework(models.Model):
    student_ID = models.ForeignKey(User)
    homeworkid = models.ForeignKey(Homework,to_field='id')
    post_time = models.DateTimeField(auto_now_add=True)
    homeworkfile = models.FileField(upload_to=homework_upload_directory_path)
    score = models.DecimalField(max_digits=4,decimal_places=1)
    classid = models.IntegerField(default=4)
    class Meta:
        db_table = 'StudentHomework'
    def __unicode__(self):
        return self.homeworkfile.name


def picture_upload_directory_path(instance,filename):
        return u'photo/user_{0}'.format(instance.tid)

class mtInfo(models.Model):
    name=models.CharField(max_length=128)
    content=models.CharField(max_length=10000)
    tid=models.CharField(max_length=128,default=0,unique=True)
    photo=models.ImageField(upload_to=picture_upload_directory_path,default='0')
    classid=models.IntegerField(default=4)
    def __unicode__(self):
        return self.picture.name
    class Meta:
        db_table='tInfo'



