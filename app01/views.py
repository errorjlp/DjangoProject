from django.core.paginator import *
from django.db.models import Q
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
    data={
        '中国': wich.objects.filter(countary__istartswith="中国").count(),
        '新加坡': wich.objects.filter(countary__istartswith="新加坡").count(),
        '马耳他': wich.objects.filter(countary__istartswith="马耳他").count(),
        '东帝汶': wich.objects.filter(countary__istartswith="东帝汶").count(),
        '泰国': wich.objects.filter(countary__istartswith="泰国").count(),
        '苏丹': wich.objects.filter(countary__istartswith="苏丹").count(),
        '佛得角': wich.objects.filter(countary__istartswith="佛得角").count(),
        '爱尔兰': wich.objects.filter(countary__istartswith="爱尔兰").count(),
        '科威特': wich.objects.filter(countary__istartswith="科威特").count(),
        '巴哈马': wich.objects.filter(countary__istartswith="巴哈马").count(),
        '巴林': wich.objects.filter(countary__istartswith="巴林").count(),
        '萨摩亚': wich.objects.filter(countary__istartswith="萨摩亚").count(),
        '安道尔': wich.objects.filter(countary__istartswith="安道尔").count(),
        '马来西亚': wich.objects.filter(countary__istartswith="马来西亚").count(),
        '德国': wich.objects.filter(countary__istartswith="德国").count(),
        '芬兰': wich.objects.filter(countary__istartswith="芬兰").count(),
        '密克罗尼西亚': wich.objects.filter(countary__istartswith="密克罗尼西亚").count(),
        '喀麦隆': wich.objects.filter(countary__istartswith="喀麦隆").count(),
        '刚果布': wich.objects.filter(countary__istartswith="刚果布").count(),
        '荷兰': wich.objects.filter(countary__istartswith="荷兰").count(),
        '贝宁': wich.objects.filter(countary__istartswith="贝宁").count(),
        '哈萨克斯坦': wich.objects.filter(countary__istartswith="哈萨克斯坦").count(),
        '巴勒斯坦': wich.objects.filter(countary__istartswith="巴勒斯坦").count(),
        '土库曼斯坦': wich.objects.filter(countary__istartswith="土库曼斯坦").count(),
        '冈比亚': wich.objects.filter(countary__istartswith="冈比亚").count(),
        '波兰': wich.objects.filter(countary__istartswith="波兰").count(),
        '瑞典': wich.objects.filter(countary__istartswith="瑞典").count(),
        '刚果金': wich.objects.filter(countary__istartswith="刚果金").count(),
        '阿尔及利亚': wich.objects.filter(countary__istartswith="阿尔及利亚").count(),
        '印度': wich.objects.filter(countary__istartswith="印度").count(),
        '阿曼': wich.objects.filter(countary__istartswith="阿曼").count(),
        '埃及': wich.objects.filter(countary__istartswith="埃及").count(),
        '克罗地亚': wich.objects.filter(countary__istartswith="克罗地亚").count(),
        '蒙古': wich.objects.filter(countary__istartswith="蒙古").count(),
        '马里': wich.objects.filter(countary__istartswith="马里").count(),
        '塞舌尔': wich.objects.filter(countary__istartswith="塞舌尔").count(),
        '阿联酋': wich.objects.filter(countary__istartswith="阿联酋").count(),
        '叙利亚': wich.objects.filter(countary__istartswith="叙利亚").count(),
        '韩国': wich.objects.filter(countary__istartswith="韩国").count(),
        '白俄罗斯': wich.objects.filter(countary__istartswith="白俄罗斯").count(),
        '俄罗斯': wich.objects.filter(countary__istartswith="俄罗斯").count(),
        '立陶宛': wich.objects.filter(countary__istartswith="立陶宛").count(),
        '拉脱维亚': wich.objects.filter(countary__istartswith="拉脱维亚").count(),
        '中非': wich.objects.filter(countary__istartswith="中非").count(),
        '巴拿马': wich.objects.filter(countary__istartswith="巴拿马").count(),
        '日本': wich.objects.filter(countary__istartswith="日本").count(),
        '毛里求斯': wich.objects.filter(countary__istartswith="毛里求斯").count(),
        '爱沙尼亚': wich.objects.filter(countary__istartswith="爱沙尼亚").count(),
        '罗马尼亚': wich.objects.filter(countary__istartswith="罗马尼亚").count(),
        '塞内加尔': wich.objects.filter(countary__istartswith="塞内加尔").count(),
        '墨西哥': wich.objects.filter(countary__istartswith="墨西哥").count(),
        '冰岛': wich.objects.filter(countary__istartswith="冰岛").count(),
        '尼日利亚': wich.objects.filter(countary__istartswith="尼日利亚").count(),
        '不丹': wich.objects.filter(countary__istartswith="不丹").count(),
        '巴基斯坦': wich.objects.filter(countary__istartswith="巴基斯坦").count(),
        '柬埔寨': wich.objects.filter(countary__istartswith="柬埔寨").count(),
        '秘鲁': wich.objects.filter(countary__istartswith="秘鲁").count(),
        '越南': wich.objects.filter(countary__istartswith="越南").count(),
        '约旦': wich.objects.filter(countary__istartswith="约旦").count(),
        '伊朗': wich.objects.filter(countary__istartswith="伊朗").count(),
        '匈牙利': wich.objects.filter(countary__istartswith="匈牙利").count(),
        '保加利亚': wich.objects.filter(countary__istartswith="保加利亚").count(),
        '巴西': wich.objects.filter(countary__istartswith="巴西").count(),
        '玻利维亚': wich.objects.filter(countary__istartswith="玻利维亚").count(),
        '塞浦路斯': wich.objects.filter(countary__istartswith="塞浦路斯").count(),
        '埃塞俄比亚': wich.objects.filter(countary__istartswith="埃塞俄比亚").count(),
        '尼加拉瓜': wich.objects.filter(countary__istartswith="尼加拉瓜").count(),
        '卢森堡': wich.objects.filter(countary__istartswith="卢森堡").count(),
        '北马其顿': wich.objects.filter(countary__istartswith="北马其顿").count(),
        '津巴布韦': wich.objects.filter(countary__istartswith="津巴布韦").count(),
        '亚美尼亚': wich.objects.filter(countary__istartswith="亚美尼亚").count(),
        '赞比亚': wich.objects.filter(countary__istartswith="赞比亚").count(),
        '阿尔巴尼亚': wich.objects.filter(countary__istartswith="阿尔巴尼亚").count(),
        '马达加斯加': wich.objects.filter(countary__istartswith="马达加斯加").count(),
        '土耳其': wich.objects.filter(countary__istartswith="土耳其").count(),
        '斯洛伐克': wich.objects.filter(countary__istartswith="斯洛伐克").count(),
        '摩尔多瓦': wich.objects.filter(countary__istartswith="摩尔多瓦").count(),
        '比利时': wich.objects.filter(countary__istartswith="比利时").count(),
        '菲律宾': wich.objects.filter(countary__istartswith="菲律宾").count(),
        '阿根廷': wich.objects.filter(countary__istartswith="阿根廷").count(),
        '突尼斯': wich.objects.filter(countary__istartswith="突尼斯").count(),
        '洪都拉斯': wich.objects.filter(countary__istartswith="洪都拉斯").count(),
        '布基纳法索': wich.objects.filter(countary__istartswith="布基纳法索").count(),
        '科特迪瓦': wich.objects.filter(countary__istartswith="科特迪瓦").count(),
        '法国': wich.objects.filter(countary__istartswith="法国").count(),
        '摩洛哥': wich.objects.filter(countary__istartswith="摩洛哥").count(),
        '柬埔寨': wich.objects.filter(countary__istartswith="柬埔寨").count(),
        #'吉尔吉斯': wich.objects.filter(countary__istartswith="吉尔吉斯").count(),
        '挪威': wich.objects.filter(countary__istartswith="挪威").count(),
        '黎巴嫩': wich.objects.filter(countary__istartswith="黎巴嫩").count(),
        '希腊': wich.objects.filter(countary__istartswith="希腊").count(),
        '毛里塔尼亚': wich.objects.filter(countary__istartswith="毛里塔尼亚").count(),
        '西班牙': wich.objects.filter(countary__istartswith="西班牙").count(),
        '危地马拉': wich.objects.filter(countary__istartswith="危地马拉").count(),
        '多米尼加': wich.objects.filter(countary__istartswith="多米尼加").count(),
        '巴拉圭': wich.objects.filter(countary__istartswith="巴拉圭").count(),
        '纳米比亚': wich.objects.filter(countary__istartswith="纳米比亚").count(),
        '吉布提': wich.objects.filter(countary__istartswith="吉布提").count(),
        '古巴': wich.objects.filter(countary__istartswith="古巴").count(),
        '尼日尔': wich.objects.filter(countary__istartswith="尼日尔").count(),
        '委内瑞拉': wich.objects.filter(countary__istartswith="委内瑞拉").count(),
        '哥斯达黎加': wich.objects.filter(countary__istartswith="哥斯达黎加").count(),
        '阿塞拜疆': wich.objects.filter(countary__istartswith="阿塞拜疆").count(),
        '乌拉圭': wich.objects.filter(countary__istartswith="乌拉圭").count(),
        '厄瓜多尔': wich.objects.filter(countary__istartswith="厄瓜多尔").count(),
        '乌兹别克斯坦': wich.objects.filter(countary__istartswith="乌兹别克斯坦").count(),
        '沙特阿拉伯': wich.objects.filter(countary__istartswith="沙特阿拉伯").count(),
        '伯利兹': wich.objects.filter(countary__istartswith="伯利兹").count(),
        '意大利': wich.objects.filter(countary__istartswith="意大利").count(),
        '肯尼亚': wich.objects.filter(countary__istartswith="肯尼亚").count(),
        '莫桑比克': wich.objects.filter(countary__istartswith="莫桑比克").count(),
        '印度尼西亚': wich.objects.filter(countary__istartswith="印度尼西亚").count(),
        '也门': wich.objects.filter(countary__istartswith="也门").count(),
        '卡塔尔': wich.objects.filter(countary__istartswith="卡塔尔").count(),
        '瑞士': wich.objects.filter(countary__istartswith="瑞士").count(),
        '苏丹': wich.objects.filter(countary__istartswith="苏丹").count(),
        '乌克兰': wich.objects.filter(countary__istartswith="乌克兰").count(),
        '葡萄牙': wich.objects.filter(countary__istartswith="葡萄牙").count(),
        '斯里兰卡': wich.objects.filter(countary__istartswith="斯里兰卡").count(),
        '哥伦比亚': wich.objects.filter(countary__istartswith="哥伦比亚").count(),
        '格鲁吉亚': wich.objects.filter(countary__istartswith="格鲁吉亚").count(),
        '阿富汗': wich.objects.filter(countary__istartswith="阿富汗").count(),
        '波斯尼亚和黑塞哥维那': wich.objects.filter(countary__istartswith="波斯尼亚和黑塞哥维那").count(),
        '捷克': wich.objects.filter(countary__istartswith="捷克").count(),
        '多哥': wich.objects.filter(countary__istartswith="多哥").count(),
        '智利': wich.objects.filter(countary__istartswith="智利").count(),
        '朝鲜': wich.objects.filter(countary__istartswith="朝鲜").count(),
        '伊拉克': wich.objects.filter(countary__istartswith="伊拉克").count(),
        '老挝': wich.objects.filter(countary__istartswith="老挝").count(),
        '丹麦': wich.objects.filter(countary__istartswith="丹麦").count(),
        '海地': wich.objects.filter(countary__istartswith="海地").count(),
        '黑山': wich.objects.filter(countary__istartswith="黑山").count(),
        '孟加拉': wich.objects.filter(countary__istartswith="孟加拉").count(),
        '乌干达': wich.objects.filter(countary__istartswith="乌干达").count(),
        '奥地利': wich.objects.filter(countary__istartswith="奥地利").count(),
        '牙买加': wich.objects.filter(countary__istartswith="牙买加").count(),
        '塔吉克斯坦': wich.objects.filter(countary__istartswith="塔吉克斯坦").count(),
        '瓦努阿图': wich.objects.filter(countary__istartswith="瓦努阿图").count(),
        '塞尔维亚': wich.objects.filter(countary__istartswith="塞尔维亚").count(),
        '几内亚': wich.objects.filter(countary__istartswith="几内亚").count(),
        '博茨瓦纳': wich.objects.filter(countary__istartswith="博茨瓦纳").count(),
        '马拉维': wich.objects.filter(countary__istartswith="马拉维").count(),
        '汤加': wich.objects.filter(countary__istartswith="汤加").count(),
        '吉尔吉斯斯坦': wich.objects.filter(countary__istartswith="吉尔吉斯斯坦").count(),
        '安哥拉': wich.objects.filter(countary__istartswith="安哥拉").count(),
    }
    print(data)
    context={
        'data':data,
    }
    return render(request,"Wmap.html",context)

def cs(request):
    return render(request,"ce.html")


def table1(request):
    return render(request, 'table_1.html')


def table1api(request):
    print(request.GET)
    #筛选逻辑
    time = request.GET.get('time')
    category = request.GET.get('category')
    region = request.GET.get('region')
    # 构造查询条件
    filters = Q()
    if time:
        filters &= Q(year=time)
    if category:
        filters &= Q(cate=category)
    if region:
        filters &= Q(region__icontains=region)

    # 执行筛选查询
    projects = cich.objects.filter(filters)

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
    print(request.GET)
    # 筛选逻辑
    gender = request.GET.get('gender')
    category = request.GET.get('category')
    region = request.GET.get('region')
    # 构造查询条件
    filters = Q()
    if gender:
        filters &= Q(gender=gender)
    if category:
        filters &= Q(category=category)
    if region:
        filters &= Q(region__icontains=region)

    # 执行筛选查询
    projects = pich.objects.filter(filters)
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