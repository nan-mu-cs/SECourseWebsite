#coding: utf-8
from datetime import time
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError
from SESite.forms import PersonUserForm, PersonProfile, CourseMaterialsForm, HomeworkForm
from SESite.models import NoticeMessage, mCourseMaterials, TAIntro, CourseIntro, Person, StudentHomework, Homework

TEACHER = 1
STUDENT = 2
'''
content_type = ContentType.objects.get(app_label="SESite",model="person")
teacher_group = Group.objects.get(name="Teacher")
teacher_group.permissions.clear()
#teacher_group.permissions.remove()
can_teach = Permission.objects.create(name="Can teach",codename="can_teach",content_type=content_type)
can_post_NoticeMessage = Permission.objects.create(name="Can post notice message",codename="can_post_NoticeMessage",
                                                   content_type=content_type)
teacher_group.permissions = [can_teach,can_post_NoticeMessage,]
#teacher_group.permissions.add(can_post_NoticeMessage)
student_group = Group.objects.get(name="Student")
student_group.permissions.clear()
can_study = Permission.objects.create(name="Can study",codename="can_study",content_type=content_type)
#student_group.permissions.add(can_study)
student_group.premissions = [can_study,]
'''

def index(request):
    '''直接返回首页，不需要任何处理'''
    return render(request,"index.html",{});


def Register(request):
    '''注册页面处理GET POST'''
    register = False
    #如果是post form
    if request.method == 'POST':
        #print request.POST
        user_form = PersonUserForm(data=request.POST)
        #print user_form
        profile_form = PersonProfile(data=request.POST)
        #系统验证表单合法
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            #profile.idnum = request.POST['idnum']
            #profile.type = request.POST['type']
            profile.save()
            register = True
            if profile.type == TEACHER:
                teacher_group = Group.objects.get(name="Teacher")
                teacher_group.user_set.add(user)
            else:
                student_group = Group.objects.get(name="Student")
                student_group.user_set.add(user)
            user = authenticate(username=request.POST['username'],password=request.POST['password'])
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            print user_form.errors, profile_form.errors
    else:
         #如果只是GET可能是单纯刷新网页，并不是提交
        user_form = PersonUserForm()
        profile_form = PersonProfile()
        #返回网页，{}里面的东西可以直接在网页中利用引用
    return render(request, 'Register.html',{'user_form':user_form,'user_profile':profile_form,'register':register})

def is_member(user,user_type):
    return user.groups.filter(name=user_type).exists()

def Login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.

        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user and is_member(user,user_type):
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your  account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'Login.html', {})

@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def NoPermission(request):
    return render(request, "NoPermission.html",{})

def NoticeBoard(request):
    #如果是老师
    if request.user.has_perm("SESite.can_teach"):
        #post 提交新内容
        if request.method == 'POST':
            #这样可以直接就插到数据库中了
            NoticeMessage.objects.create(writer=request.user,message = request.POST['post_message'])
        #如果是GET，可能是刷新网页，也可能是点了删除链接
        elif request.method == 'GET':
            try:
                #删除信息
                messageid = request.GET['deleteid']
                try:
                    #数据库中查询
                    query = NoticeMessage.objects.get(id=messageid).delete()
                except NoticeMessage.DoesNotExist:
                    #查询结果为空会抛出异常，需要在异常中处理
                    query = None
            except MultiValueDictKeyError:
                #单纯刷新网页，所以不会GET到deleteid
                messageid = None
    #数据库中现在存在的所有message都get出来
    result = []
    message_list = NoticeMessage.objects.all()
    message_list.order_by("post_time")
    for item in message_list:
        res = [item.id,item.writer.username,item.message,item.post_time.strftime("%Y-%m-%d %H:%M:%S")]
        result.append(res)
    result.reverse()
    return render(request,"NoticeBoard.html",{'message':result})

def CourseMaterials(request):
    '''用来处理资料上传、下载'''
    '''判断老师可以上传资料'''
    if request.user.has_perm("SESite.can_teach"):
        '''通过表单上传文件'''
        if request.method == 'POST':
            '''获得表单'''
            form = CourseMaterialsForm(request.POST,request.FILES)
            '''检查表单合法性'''
            if form.is_valid():
                '''将数据存入数据库，会自动存储文件'''
                newdoc = mCourseMaterials(user=request.user,docfile=request.FILES['docfile'],title=request.FILES['docfile'].name)
                newdoc.save()
                return HttpResponseRedirect('CourseMaterials')
        elif request.method == 'GET':
            '''get方法可能是刷新网页，也可能是删除'''
            try:
                '''如果是删除，获取删除文件id'''
                fileid = request.GET['deleteid']
                try:
                    '''从数据库中删掉，若记录不存在抛出mCourseMaterials.DoesNotExist异常'''
                    query = mCourseMaterials.objects.get(id=fileid).delete()
                except mCourseMaterials.DoesNotExist:
                    query = None
            except MultiValueDictKeyError:
                fileid = None
    '''普通用GET方法获取网页'''
    form = CourseMaterialsForm()
    documents = mCourseMaterials.objects.all()
    return render(request,'CourseMaterials.html',{'documents':documents,'form':form})

@receiver(pre_delete, sender=mCourseMaterials)
def mCourseMaterials_delete(sender, instance, **kwargs):
    '''删除文件记录时，会接收文件删除信号，同时删除实际存在的文件'''
    # Pass false so FileField doesn't save the model.
    instance.docfile.delete(False)


def CourseMaterials_preview(request,fileid):
    try:
        docfile = mCourseMaterials.objects.get(id=fileid)
        return pdf_preview(request,docfile.docfile._get_path())
    except mCourseMaterials.DoesNotExist:
        docfile = None
        return HttpResponseRedirect('CourseMaterials.html')

def pdf_preview(request,filepath):
    with open(filepath,'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed
def Course_Intro(request):
    if request.user.has_perm("SESite.can_teach"):
        if request.method == 'POST':

            CourseIntro.objects.create(writer=request.user,pre_intro=request.POST['PreCourseRequire'],materi_intro=request.POST['Material'],score_consti=request.POST['Score'])
            # print pre_intro
            # print message
            # print score_consti
            # print materi_intro
            print 'demo'
        #如果是GET，可能是刷新网页，也可能是点了删除链接,score_consti=request['Score'],materi_intro=request.POST['Material'],message=request['msg']
        elif request.method == 'GET':
            try:
                #删除信息
                pre_introid = request.GET['deleteid']
                # print 'pre_introid = ' + pre_introid3
                try:
                    #数据库中查询
                    query = CourseIntro.objects.get(id=pre_introid).delete()
                except CourseIntro.DoesNotExist:
                    #查询结果为空会抛出异常，需要在异常中处理
                    query = None
            except MultiValueDictKeyError:
                #单纯刷新网页，所以不会GET到deleteid/
                pre_introid = 0

    result = []
    message_list = CourseIntro.objects.all()
    message_list.order_by('post_time')
    # 每次刷新或者输入新的预修要求，会显示最新的要求，历史依旧存在数据库当中
    for item in message_list:
        res = [item.id, item.writer.username, item.pre_intro, item.materi_intro, item.score_consti]
        result.append(res)
    # result.reverse()
    print '******************'
    print result
    print '******************'
    return render(request,"CourseIntro.html", {'pre_intro': result})

def TA_Intro(request):
    if request.user.has_perm("SESite.can_teach"):
        if request.method == 'POST':

            TAIntro.objects.create(writer=request.user,teacher_intro=request.POST['teacher_msg'],ta_intro=request.POST['ta_msg'])
            # print pre_intro
            # print message
            # print score_consti
            # print materi_intro
            print 'demo'
        #如果是GET，可能是刷新网页，也可能是点了删除链接,score_consti=request['Score'],materi_intro=request.POST['Material'],message=request['msg']
        elif request.method == 'GET':
            try:
                #删除信息
                teacher_introid = request.GET['deleteid']
                # print 'pre_introid = ' + pre_introid3
                try:
                    #数据库中查询
                    query = TAIntro.objects.get(id=teacher_introid).delete()
                except TAIntro.DoesNotExist:
                    #查询结果为空会抛出异常，需要在异常中处理
                    query = None
            except MultiValueDictKeyError:
                #单纯刷新网页，所以不会GET到deleteid
                teacher_introid = 0

    result = []
    message_list = TAIntro.objects.all()
    message_list.order_by('post_time')
    # 每次刷新或者输入新的预修要求，会显示最新的要求，历史依旧存在数据库当中
    for item in message_list:
        res = [item.id, item.writer.username, item.teacher_intro, item.ta_intro]
        result.append(res)
    # result.reverse()
    print '******************'
    print result
    print '******************'
    return render(request,"TAIntro.html", {'teacher_intro': result})

def Account_Info(request):
    try:
        account_data = Person.objects.get(user=request.user)
    except Person.DoesNotExist:
        account_data = None
    return render(request,"AccountInfo.html",{"account_data":account_data})

def Change_Account(request):
    print request.POST
    if request.POST['email_value'] != "":
        User.objects.filter(username=request.user.username).update(email=request.POST['email_value'])
    if request.POST['psw_value'] != "":
        User.objects.filter(username=request.user.username).update(password=request.POST['psw_value'])
    try:
        account_data = Person.objects.get(user=request.user)
    except Person.DoesNotExist:
        account_data = None
    return HttpResponse(account_data.user.email)

def AssignHomework(request):
    #post 提交新内容
    if request.method == 'POST':
        #这样可以直接就插到数据库中了
        try:
            tube = StudentHomework.objects.get(id=request.POST['HomeworkID'])
            tube.score = request.POST['score']
            tube.save();
        except MultiValueDictKeyError:
            Homework.objects.create(assigner=request.user,description = request.POST['post_message'],due_time = request.POST['due_time'],title=request.POST['title'])
        #如果是GET，可能是刷新网页，也可能是点了删除链接
    elif request.method == 'GET':
        try:
            #删除信息
            messageid = request.GET['deleteid']
            try:
                #数据库中查询
                query = Homework.objects.get(id=messageid).delete()
            except NoticeMessage.DoesNotExist:
                #查询结果为空会抛出异常，需要在异常中处理
                query = None
        except MultiValueDictKeyError:
            #单纯刷新网页，所以不会GET到deleteid
            messageid = None
    #数据库中现在存在的所有message都get出来
    result = []
    message_list = Homework.objects.all()
    message_list.order_by("post_time")
    for item in message_list:
        res = [item.id,item.assigner,item.description,item.due_time.strftime("%Y-%m-%d %H:%M:%S"),item.title]
        result.append(res)
    result.reverse()
    homeworks = []
    homeworks_list = StudentHomework.objects.all()
    homeworks_list.order_by("homeworkid")
    for item in homeworks_list:
        res = [item.homeworkid_id,item.student_ID, item.homeworkfile,item.score,item.id]
        homeworks.append(res)

    return render(request,"AssignHomework.html",{'message':result,'homeworks':homeworks})

def Grade(request):
    if request.method == 'POST':
        print(request.POST['HomeworkID'])
        tube = StudentHomework.objects.get(id=request.POST['HomeworkID'])
        tube.score = request.POST['score']
        tube.save();
    student_gourp_list=StudentHomework.objects.all().values('student_ID__username').annotate(s_amount = Sum('score'))
    score_list = StudentHomework.objects.all()
    score_list.order_by("homeworkid_id")
    Sumscore=[]
    ScoreList=[]
    for item in student_gourp_list:
        res = [str(item["s_amount"]),str(item["student_ID__username"])]
        Sumscore.append(res)
    for item in score_list:
        res = [item.score,str(item.student_ID),item.homeworkid_id,item.id]
        ScoreList.append(res)
    return render(request, 'Grade.html',{'StudentScore':Sumscore,'HomeworkScore':ScoreList})

def ShowGrade(request):
    result = []
    message_list = StudentHomework.objects.filter(student_ID=request.user)
    message_list.order_by("homeworkid")
    for item in message_list:
        res = [item.homeworkid_id,item.score]
        result.append(res)
    return render(request, 'ShowGrade.html',{'message':result})

def HomeworkAndGrades(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST,request.FILES)
        if form.is_valid():
            homework=Homework.objects.get(id=request.POST['hwid'])
            newdoc = StudentHomework(student_ID=request.user,homeworkid=homework,homeworkfile=request.FILES['docfile'],score=0)
            newdoc.save()
            return HttpResponseRedirect('HomeworkAndGrades')
    elif request.method == 'GET':
        try:
            #删除信息
            messageid = request.GET['deleteid']
            try:
                #数据库中查询
                query = StudentHomework.objects.get(id=messageid).delete()
            except NoticeMessage.DoesNotExist:
                #查询结果为空会抛出异常，需要在异常中处理
                query = None
        except MultiValueDictKeyError:
            #单纯刷新网页，所以不会GET到deleteid
            messageid = None
    #数据库中现在存在的所有message都get出来
    result = []
    message_list = Homework.objects.all()
    message_list.order_by("post_time")
    for item in message_list:
        res = [item.id,item.assigner,item.description,item.due_time.strftime("%Y-%m-%d %H:%M:%S"),item.title]
        result.append(res)
    result.reverse()
    homeworks = []
    form = HomeworkForm()
    documents = StudentHomework.objects.filter(student_ID=request.user)
    for item in documents:
        res = [item.homeworkid_id,item.homeworkfile,item.id]
        homeworks.append(res)
    print (homeworks)
    return render(request,"HomeworkAndGrades.html",{'message':result, 'form':form, 'homeworks':homeworks})

