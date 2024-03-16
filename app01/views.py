from django.core.paginator import *
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
from .models import cich,pich,lich,cnum,wich
from django.core import serializers

import json
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the")



def home(request):
    #优先去根目录寻找
    #根据app注册顺序逐一去templates目录下找需要的文件

    return render(request,"home.html")

def cm(request):
    # 从传承人名单中获取每个类别的传承人个数 饼图
    data_1 = {
        '民间文学': pich.objects.filter(category__istartswith="民间文学").count(),
        '传统音乐': pich.objects.filter(category__istartswith="传统音乐").count(),
        '传统舞蹈': pich.objects.filter(category__istartswith="传统舞蹈").count(),
        '传统戏剧': pich.objects.filter(category__istartswith="传统戏剧").count(),
        '曲艺': pich.objects.filter(category__istartswith="曲艺").count(),
        '传统体育、游艺与杂技': pich.objects.filter(category__istartswith="传统体育、游艺与杂技").count(),
        '传统美术': pich.objects.filter(category__istartswith="传统美术").count(),
        '传统技艺': pich.objects.filter(category__istartswith="传统技艺").count(),
        '传统医药': pich.objects.filter(category__istartswith="传统医药").count(),
        '民俗': pich.objects.filter(category__istartswith="民俗").count(),
    }
    # 各省示范区数据 柱状图
    data_2 = {
        '北京市': lich.objects.filter(city__istartswith="北京市").count(),
        '天津市': lich.objects.filter(city__istartswith="天津市").count(),
        '河北省': lich.objects.filter(city__istartswith="河北省").count(),
        '山西省': lich.objects.filter(city__istartswith="山西省").count(),
        '内蒙古自治区': lich.objects.filter(city__istartswith="内蒙古自治区").count(),
        '辽宁省': lich.objects.filter(city__istartswith="辽宁省").count(),
        '吉林省': lich.objects.filter(city__istartswith="吉林省").count(),
        '黑龙江省': lich.objects.filter(city__istartswith="黑龙江省").count(),
        '上海市': lich.objects.filter(city__istartswith="上海市").count(),
        '江苏省': lich.objects.filter(city__istartswith="江苏省").count(),
        '浙江省': lich.objects.filter(city__istartswith="浙江省").count(),
        '安徽省': lich.objects.filter(city__istartswith="安徽省").count(),
        '福建省': lich.objects.filter(city__istartswith="福建省").count(),
        '江西省': lich.objects.filter(city__istartswith="江西省").count(),
        '山东省': lich.objects.filter(city__istartswith="山东省").count(),
        '河南省': lich.objects.filter(city__istartswith="河南省").count(),
        '湖北省': lich.objects.filter(city__istartswith="湖北省").count(),
        '湖南省': lich.objects.filter(city__istartswith="湖南省").count(),
        '广东省': lich.objects.filter(city__istartswith="广东省").count(),
        '广西壮族自治区': lich.objects.filter(city__istartswith="广西壮族自治区").count(),
        '海南省': lich.objects.filter(city__istartswith="海南省").count(),
        '重庆市': lich.objects.filter(city__istartswith="重庆市").count(),
        '四川省': lich.objects.filter(city__istartswith="四川省").count(),
        '贵州省': lich.objects.filter(city__istartswith="贵州省").count(),
        '云南省': lich.objects.filter(city__istartswith="云南省").count(),
        '西藏自治区': lich.objects.filter(city__istartswith="西藏自治区").count(),
        '陕西省': lich.objects.filter(city__istartswith="陕西省").count(),
        '甘肃省': lich.objects.filter(city__istartswith="甘肃省").count(),
        '青海省': lich.objects.filter(city__istartswith="青海省").count(),
        '宁夏回族自治区': lich.objects.filter(city__istartswith="宁夏回族自治区").count(),
        '新疆维吾尔自治区': lich.objects.filter(city__istartswith="新疆维吾尔自治区").count(),
        '香港特别行政区': lich.objects.filter(city__istartswith="香港特别行政区").count(),
        '澳门特别行政区': lich.objects.filter(city__istartswith="澳门特别行政区").count(),
        '台湾省': lich.objects.filter(city__istartswith="台湾省").count(),
    }
    # 各省非遗数据 中国地图
    data_3 = {
        '北京': cich.objects.filter(region__istartswith="北京市").count(),
        '天津': cich.objects.filter(region__istartswith="天津市").count(),
        '河北': cich.objects.filter(region__istartswith="河北省").count(),
        '山西': cich.objects.filter(region__istartswith="山西省").count(),
        '内蒙古': cich.objects.filter(region__istartswith="内蒙古自治区").count(),
        '辽宁': cich.objects.filter(region__istartswith="辽宁省").count(),
        '吉林': cich.objects.filter(region__istartswith="吉林省").count(),
        '黑龙江': cich.objects.filter(region__istartswith="黑龙江省").count(),
        '上海': cich.objects.filter(region__istartswith="上海市").count(),
        '江苏': cich.objects.filter(region__istartswith="江苏省").count(),
        '浙江': cich.objects.filter(region__istartswith="浙江省").count(),
        '安徽': cich.objects.filter(region__istartswith="安徽省").count(),
        '福建': cich.objects.filter(region__istartswith="福建省").count(),
        '江西': cich.objects.filter(region__istartswith="江西省").count(),
        '山东': cich.objects.filter(region__istartswith="山东省").count(),
        '河南': cich.objects.filter(region__istartswith="河南省").count(),
        '湖北': cich.objects.filter(region__istartswith="湖北省").count(),
        '湖南': cich.objects.filter(region__istartswith="湖南省").count(),
        '广东': cich.objects.filter(region__istartswith="广东省").count(),
        '广西': cich.objects.filter(region__istartswith="广西壮族自治区").count(),
        '海南': cich.objects.filter(region__istartswith="海南省").count(),
        '重庆': cich.objects.filter(region__istartswith="重庆市").count(),
        '四川': cich.objects.filter(region__istartswith="四川省").count(),
        '贵州': cich.objects.filter(region__istartswith="贵州省").count(),
        '云南': cich.objects.filter(region__istartswith="云南省").count(),
        '西藏': cich.objects.filter(region__istartswith="西藏自治区").count(),
        '陕西': cich.objects.filter(region__istartswith="陕西省").count(),
        '甘肃': cich.objects.filter(region__istartswith="甘肃省").count(),
        '青海': cich.objects.filter(region__istartswith="青海省").count(),
        '宁夏': cich.objects.filter(region__istartswith="宁夏回族自治区").count(),
        '新疆': cich.objects.filter(region__istartswith="新疆维吾尔自治区").count(),
        '香港': cich.objects.filter(region__istartswith="香港特别行政区").count(),
        '澳门': cich.objects.filter(region__istartswith="澳门特别行政区").count(),
        '台湾': cich.objects.filter(region__istartswith="台湾省").count(),
    }
    data_4 = {
        '民间文学': cich.objects.filter(cate__istartswith="民间文学").count(),
        '传统音乐': cich.objects.filter(cate__istartswith="传统音乐").count(),
        '传统舞蹈': cich.objects.filter(cate__istartswith="传统舞蹈").count(),
        '传统戏剧': cich.objects.filter(cate__istartswith="传统戏剧").count(),
        '曲艺': cich.objects.filter(cate__istartswith="曲艺").count(),
        '传统体育、游艺与杂技': cich.objects.filter(cate__istartswith="传统体育、游艺与杂技").count(),
        '传统美术':cich.objects.filter(cate__istartswith="传统美术").count(),
        '传统技艺': cich.objects.filter(cate__istartswith="传统技艺").count(),
        '传统医药': cich.objects.filter(cate__istartswith="传统医药").count(),
        '民俗': cich.objects.filter(cate__istartswith="民俗").count(),
    }
    context = {
        'data_1':data_1,
        'data_2':data_2,
        'data_3':data_3,
        'data_4':data_4
    }
    return render(request,"Cmap.html",context)

def wm(request):
    return render(request,"Wmap.html")

def cs(request):
    return render(request,"ce.html")


def table1(request):
    return render(request, 'table_1.html')


def table1api(request):
    projects = cich.objects.all()
    paginator = Paginator(projects, 10)

    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    # 手动构建JSON数据列表
    data_list = []
    for project in page_obj:
        data_list.append({
            'id': project.id,
            'bid': project.bid,
            'name': project.name,
            'cate': project.cate,
            'year': project.year,
            'region': project.region,
            'institution': project.institution
        })

        # 返回JSON响应，包括数据和分页信息
    return JsonResponse({
        'data': data_list,
        'total_pages': paginator.num_pages,
        'current_page': page_obj.number
    })

def table2(request):
    return render(request, 'table_2.html')
def table2api(request):
    projects = pich.objects.all()
    paginator = Paginator(projects, 10)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # 手动构建JSON数据列表
    data_list = []
    for project in page_obj:
        data_list.append({
            'id': project.id,
            'name': project.name,
            'gender': project.gender,
            'nation': project.nation,
            'category': project.category,
            'bid': project.bid,
            'pname': project.pname,
            'region': project.region
        })

        # 返回JSON响应，包括数据和分页信息
    return JsonResponse({
        'data': data_list,
        'total_pages': paginator.num_pages,
        'current_page': page_obj.number
    })

def table3(request):
    return render(request, 'table_3.html')

def table3api(request):
    projects = lich.objects.all()
    paginator = Paginator(projects, 10)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # 手动构建JSON数据列表
    data_list = []
    for project in page_obj:
        data_list.append({
            'id': project.id,
            'city': project.city,
            'location': project.location,
            'category': project.category,
            'name': project.name
        })

        # 返回JSON响应，包括数据和分页信息
    return JsonResponse({
        'data': data_list,
        'total_pages': paginator.num_pages,
        'current_page': page_obj.number
    })
def table4(request):
    projects = cnum.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'table_4.html', context)

def search(request):
    keyword = request.GET.get('keyword', '')
    queryset = cich.objects.all()

    if keyword:
        queryset = queryset.filter(name__icontains=keyword)  # 以名字字段为例进行模糊搜索

    context = {'objects': queryset}

    return render(request, 'search.html',context)