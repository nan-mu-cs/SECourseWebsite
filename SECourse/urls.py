"""SECourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
import postman
from SECourse import settings
from SESite import views
from SESite.admin import admin_site
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myadmin/', admin_site.urls),
    url(r'^$',views.index,name="index"),
    url(r'^Register$',views.Register,name="Register"),
    url(r'^Login',views.Login,name="Login"),
    url(r'^Logout',views.Logout,name="Logout"),
    url(r'nopremission',views.NoPermission,name="NoPermission"),
    url(r'^NoticeBoard$',views.NoticeBoard,name="NoticeBoard"),
    url(r'CourseMaterials$',views.CourseMaterials,name="CourseMaterials"),
    url(r'CourseMaterialspdfpreview(?P<fileid>\d+)$',views.CourseMaterials_preview,name="pdf_preview"),
    url(r'ScoreConsti$', views.Course_Intro, name="CourseIntro"),
    url(r'CourseIntro$', views.Course_Intro, name="CourseIntro"),
    url(r'TAIntro$', views.TA_Intro, name="TAIntro"),
    url(r'teacher_msg$', views.TA_Intro, name="TAIntro"),
    url(r'ta_msg$', views.TA_Intro, name="TAIntro"),
    url(r'AccountInfo$',views.Account_Info,name="AccountInfo"),
    url(r'change_account$',views.Change_Account,name="Change_Account"),
    url(r'AssignHomework$',views.AssignHomework,name="AssignHomework"),
    url(r'^Grade$',views.Grade,name="Grade"),
    url(r'HomeworkAndGrades$',views.HomeworkAndGrades,name="HomeworkAndGrades"),
    url(r'^ShowGrade$',views.ShowGrade,name="ShowGrade"),
    url(r'ChooseClass$',views.ChooseClass,name="ChooseClass"),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
