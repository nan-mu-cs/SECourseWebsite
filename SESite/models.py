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
