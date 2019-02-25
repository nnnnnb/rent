# coding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

STATUSCHOICE = (
    ('1', '已发布'),
    ('0', '未发布'),
)

class House_facilities(models.Model):
    house = models.ForeignKey('House', on_delete=models.CASCADE)
    facilities = models.ForeignKey('Facilities', on_delete=models.CASCADE)

class Community_traffic(models.Model):
    community = models.ForeignKey('Community', on_delete=models.CASCADE)
    traffic = models.ForeignKey('Traffic', on_delete=models.CASCADE)

class House(models.Model):
    community = models.ForeignKey('Community', verbose_name='所属小区')
    title = models.CharField(max_length=50, verbose_name='房屋标题')
    keyword = models.CharField(max_length=100, verbose_name='房屋关键字')
    rental = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='租金')
    bedroom = models.CharField(max_length=5, verbose_name='卧室')
    livingroom = models.CharField(max_length=5, verbose_name='客厅')
    toilet = models.CharField(max_length=5, verbose_name='卫生间')
    imgurl = models.ImageField(upload_to='media/images/house', verbose_name='图片路径')
    facilities = models.ManyToManyField('Facilities', null=True, blank=True, verbose_name='配套设施')
    balcony = models.CharField(max_length=5, null=True, blank=True, verbose_name='阳台')
    building = models.CharField(max_length=5, null=True, blank=True, verbose_name='栋')
    unit = models.CharField(max_length=5, null=True, blank=True, verbose_name='单元')
    storey = models.CharField(max_length=5, null=True, blank=True, verbose_name='层')
    room = models.CharField(max_length=5, null=True, blank=True, verbose_name='房号')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='联系方式')
    fitment = models.CharField(max_length=1, choices=settings.FITMENT, default=0, null=True, blank=True,  verbose_name='装修类型')
    orientation = models.CharField(max_length=2, choices=settings.ORIENTATION, default=0, null=True, blank=True,  verbose_name='朝向')
    storey_total = models.IntegerField(null=True, blank=True, verbose_name='总楼层')
    storey_property = models.CharField(max_length=1, choices=settings.STOREY_PROPERTY, default=0, null=True, blank=True, verbose_name='楼层类型')
    pay_method = models.CharField(max_length=2, choices=settings.PAY_METHOD, default=0, null=True, blank=True, verbose_name='支付方式')
    acreage = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='面积')
    number = models.CharField(max_length=5, null=True, blank=True, verbose_name='房屋编号')
    status = models.CharField(max_length=1, choices=STATUSCHOICE, default=0, verbose_name='状态')

    class Meta:
        verbose_name = ('房屋')
        verbose_name_plural = ('房屋管理')

    def __str__(self):
        return self.title


class Housealbum(models.Model):
    house = models.ForeignKey('House', verbose_name='房屋名称')
    name = models.CharField(max_length=100, verbose_name='图片名称')
    sort = models.IntegerField(null=True, blank=True, verbose_name='排序')
    imgurl = models.ImageField(upload_to='media/images/housealbum', verbose_name='图片路径')
    status = models.CharField(max_length=1, choices=STATUSCHOICE, default=0, verbose_name='状态')

    class Meta:
        verbose_name = ('房屋图片')
        verbose_name_plural = ('房屋图片管理')

    def __str__(self):
        return '<img src="%s">' % self.imgurl


class Facilities(models.Model):
    name = models.CharField(max_length=50, verbose_name='设施名称')
    imgurl = models.ImageField(upload_to='media/images/facilities', null = True, blank = True, verbose_name='图片路径')

    class Meta:
        verbose_name = ('配套设施')
        verbose_name_plural = ('配套设施管理')

    def __str__(self):
        return self.name



class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name='行政区名称')
    sort = models.IntegerField(null=True, blank=True, verbose_name='排序')
    status = models.CharField(max_length=1, choices=STATUSCHOICE, default=0, verbose_name='状态')

    class Meta:
        verbose_name = ('行政区')
        verbose_name_plural = ('行政区管理')

    def __str__(self):
        return self.name


class Block(models.Model):
    region = models.ForeignKey('Region', verbose_name='所属区域')
    name = models.CharField(max_length=50, verbose_name='商圈名称')
    sort = models.IntegerField(null=True, blank=True, verbose_name='排序')
    status = models.CharField(max_length=1, choices=STATUSCHOICE, default=0, verbose_name='状态')

    class Meta:
        verbose_name = ('商圈')
        verbose_name_plural = ('商圈管理')

    def __str__(self):
        return self.name




class Community(models.Model):
    name = models.CharField(max_length=100, verbose_name='小区名称')
    traffic = models.ManyToManyField('Traffic', verbose_name='轨道交通')
    region = models.ForeignKey('Region', verbose_name='所属区域')
    block = models.ForeignKey('Block', verbose_name='所属商圈')
    address = models.CharField(max_length=50, verbose_name='地址')
    acreage = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='占地面积')
    park_space = models.CharField(max_length=255,null=True, blank=True, verbose_name='停车位')  # 停车位
    green_rate = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='绿化率')
    volume_rate = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='容积率')
    build_type = models.CharField(max_length=40, null=True, blank=True, verbose_name='建筑类型')
    build_years = models.CharField(max_length=20, null=True, blank=True, verbose_name='建成年份')
    build_area = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='建筑面积')
    house_count = models.IntegerField(null=True, blank=True, verbose_name='房屋套数')
    property_type = models.CharField(max_length=40, null=True, blank=True, verbose_name='产权类型')
    property_years = models.CharField(max_length=20, null=True, blank=True, verbose_name='产权年限')
    property_company = models.CharField(max_length=40, null=True, blank=True, verbose_name='物业公司')
    developers = models.CharField(max_length=40, null=True, blank=True, verbose_name='开发商')
    property_costs = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='物业价格')
    property_tel = models.CharField(max_length=40, null=True, blank=True, verbose_name='物业电话')
    property_addr = models.CharField(max_length=100, null=True, blank=True, verbose_name='物业地址')
    lat = models.CharField(max_length=15, null=True, blank=True, verbose_name='纬度')
    lon = models.CharField(max_length=15, null=True, blank=True, verbose_name='经度')

    class Meta:
        verbose_name = ('小区')
        verbose_name_plural = ('小区管理')

    def __str__(self):
        return self.name

class Traffic(models.Model):
    name = models.CharField(max_length=50, verbose_name='轨道交通名称')
    sort = models.IntegerField(null=True, blank=True, verbose_name='排序')
    status = models.CharField(max_length=1, choices=STATUSCHOICE, default=0, verbose_name='状态')

    class Meta:
        verbose_name = ('轨道交通')
        verbose_name_plural = ('轨道交通管理')

    def __str__(self):
        return self.name


class Lifetype(models.Model):
    name = models.CharField(max_length=50, verbose_name='类型名称')
    sort = models.IntegerField(null=True, blank=True, verbose_name='排序')
    status = models.CharField(max_length=1, choices=STATUSCHOICE, default=0, verbose_name='状态')

    class Meta:
        verbose_name = ('租房生活类型')
        verbose_name_plural = ('租房生活类型管理')

    def __str__(self):
        return self.name

class Life(models.Model):
    lifetype = models.ForeignKey('Lifetype', verbose_name='所属类型')
    title = models.CharField(max_length=100, verbose_name='房屋标题')
    # content = models.TextField(verbose_name='正文内容')
    content = RichTextUploadingField(verbose_name='正文')
    keyword = models.CharField(max_length=100, verbose_name='房屋关键字')
    imgurl = models.ImageField(upload_to='media/images/life', null=True, blank=True, verbose_name='图片路径')
    click = models.IntegerField(null=True, blank=True, verbose_name='点击量')
    status = models.CharField(max_length=1, choices=STATUSCHOICE, default=0, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='保存时间')
    class Meta:
        verbose_name = ('租房生活')
        verbose_name_plural = ('租房生活管理')

    def __str__(self):
        return self.title

USERCHOICE = (
    ('1', '已启用'),
    ('0', '已冻结'),
)


class Customer(models.Model):
    account = models.CharField(max_length=50, verbose_name='账户名')
    password = models.CharField(max_length=50, verbose_name='密码')
    realname = models.CharField(max_length=50, verbose_name='真实姓名')
    status = models.CharField(max_length=1, choices=USERCHOICE, default=0, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='保存时间')

    class Meta:
        verbose_name = ('客户')
        verbose_name_plural = ('客户注册管理')

    def __str__(self):
        return self.account

