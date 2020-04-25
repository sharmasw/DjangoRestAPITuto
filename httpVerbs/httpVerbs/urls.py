"""httpVerbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from firstPage import views
from django.views.decorators.csrf import csrf_exempt
from firstPage.views import AppAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    url('index',views.index,name='Demo index'),
    # url('classINdex',csrf_exempt(AppAPI.as_view()),name='Demo index'),
    url('postINdex',csrf_exempt(views.postINdex),name='Demo index'),
    url('recordAll',views.recordAll,name='Demo index'),
    path('record',csrf_exempt(AppAPI.as_view()),name='Demo index'),
    path('record/<userID>',csrf_exempt(AppAPI.as_view()),name='Demo index'),
]