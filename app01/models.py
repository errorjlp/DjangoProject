from django.db import models


# Create your models here.
#非遗名录
class cich(models.Model):
    # 序号
    id = models.IntegerField(max_length=10,primary_key=True)
    # 项目编号（罗马数字+阿拉伯数字）
    bid = models.CharField(max_length=10)
    # 项目名称
    name = models.CharField(max_length=50)
    # 所属类别（民间文学、传统音乐等）
    cate = models.CharField(max_length=20)
    # 入选批次及年份
    year = models.CharField(max_length=20)
    # 地区（省/自治区/直辖市）
    region = models.CharField(max_length=100)
    # 文化遗产保护机构
    institution = models.CharField(max_length=100)

#传承人
class pich(models.Model):
    # 编号
    id = models.IntegerField(max_length=20, primary_key=True)  # 如：01-0001
    # 姓名
    name = models.CharField(max_length=20)
    # 性别
    gender = models.CharField(max_length=2)  # 一般使用'M'表示男，'F'表示女
    # 民族
    nation = models.CharField(max_length=10)
    # 所属类别（民间文学、传统音乐等）
    category = models.CharField(max_length=20)
    # 国家级名录项目编号（罗马数字+阿拉伯数字）
    bid = models.CharField(max_length=10)
    # 国家级名录项目名称
    pname = models.CharField(max_length=50)
    # 所在地区（省/自治区/直辖市）
    region = models.CharField(max_length=50)

#示范区
class lich(models.Model):
    # 序号
    id = models.IntegerField(max_length=10, primary_key=True)
    # 省份
    city = models.CharField(max_length=20)
    # 基地
    location = models.CharField(max_length=50)
    # 项目类别
    category = models.CharField(max_length=20)
    # 名称
    name = models.CharField(max_length=50)

#中国入选
class cnum(models.Model):
    # 序号
    id = models.IntegerField(max_length=10, primary_key=True)
    # 时间
    time = models.CharField(max_length=20)
    # 类别
    bie = models.CharField(max_length=30)
    # 类型
    category = models.CharField(max_length=30)

#联合国
class wich(models.Model):
    # 名称
    name = models.CharField(max_length=1000)
    # 国家
    countary = models.CharField(max_length=100)

