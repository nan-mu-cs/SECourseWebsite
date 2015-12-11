# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User)
    idnum = models.CharField(max_length=20,primary_key=True)
    type = models.IntegerField()
    class Meta:
         db_table = 'Person'
    def __unicode__(self):
        return self.idnum

class NoticeMessage(models.Model):
    writer = models.ForeignKey(User)
    message = models.CharField(max_length=2000)
    post_time = models.DateTimeField(auto_now_add=True)
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
    class Meta:
        db_table = 'CourseIntro'
    def __unicode__(self):
        return self.pre_intro

class TAIntro(models.Model):
    writer = models.ForeignKey(User)
    teacher_intro = models.CharField(max_length=2000)
    ta_intro = models.CharField(max_length = 2000)
    post_time = models.DateTimeField(auto_now_add = True)
    class Meta:
        db_table = 'TAIntro'
    def __unicode__(self):
        return self.teacher_intro
