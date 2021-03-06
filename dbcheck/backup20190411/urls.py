"""db_check URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'dbcheck'
urlpatterns = [
    path('home/', views.home, name='主页'),
    path('checkpage/', views.checkpage, name='检查页面'),
    path('checkpage146245/', views.checkpage146245),
    # path('about/', views.about, name='关于本站'),
    # path('edit/<每一件事_id>', views.edit, name='编辑'),
    # path('del/<每一件事_id>', views.delete, name='删除'),
    # path('cross/<每一件事_id>', views.cross, name='划掉'),
]
