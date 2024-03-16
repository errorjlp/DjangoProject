"""DProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from app01 import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index/', views.index),
    path('Cmap/',views.cm,name='cm'),
    path('home/',views.home),
    path('ce/',views.cs,name='cs'),
    path('table1/',views.table1,name='table1'),
    path('table2/',views.table2,name='table2'),
    path('table3/',views.table3,name='table3'),
    path('table1api/',views.table1api),
    path('table2api/',views.table2api),
    path('table3api/',views.table3api),
    path('table4/',views.table4,name='table4'),
    path('Wmap/',views.wm,name='wm'),
    path('search/',views.search,name='search'),
]
