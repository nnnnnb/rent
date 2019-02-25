from django.contrib import admin
from .models import * #导入数据库
# Register your models here.

admin.site.site_header = '租房网后台管理系统'
admin.site.site_title = '租房管理系统'

class CommunityAdmin(admin.ModelAdmin):
    change_form_template = 'region_block_linkage.html'
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('name', 'address', 'lat', 'lon')
    #list_per_page 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)
    ##list_editable 设置默认可编辑字段MEDIA_URL
    list_editable = ['address','lat','lon']

    # 过滤器
    list_filter = ('block', )  # 过滤器
    #搜索字段
    search_fields = ('name', 'address')
    # date_hierarchy = 'go_time'  # 详细时间分层筛选
admin.site.register(Community,CommunityAdmin)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort', 'status')
    list_per_page = 10
    ordering = ('-sort','-id')
    list_editable = ['sort', 'status']
    list_filter = ('status',)
    search_fields = ('name',)
admin.site.register(Region,RegionAdmin)

class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'sort', 'status')
    list_per_page = 10
    ordering = ('-sort','-id')
    list_editable = ['region', 'sort', 'status']
    list_filter = ('region', 'status')
    search_fields = ('name',)
admin.site.register(Block,BlockAdmin)

class TrafficAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort', 'status')
    list_per_page = 10
    ordering = ('-sort', '-id')
    list_editable = ['sort', 'status']
    list_filter = ('status',)
    search_fields = ('name',)
admin.site.register(Traffic, TrafficAdmin)

class FacilitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'imgurl')
    list_per_page = 10
admin.site.register(Facilities, FacilitiesAdmin)

class HouseAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('title', 'bedroom', 'livingroom', 'toilet', 'status')
    #list_per_page 设置每页显示多少条记录，默认是100条
    list_per_page = 10
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)
    ##list_editable 设置默认可编辑字段
    list_editable = ['bedroom','livingroom','toilet', 'status']

    # 过滤器
    list_filter = ('status', 'community', )  # 过滤器
    #搜索字段
    search_fields = ('title',)
    # date_hierarchy = 'go_time'  # 详细时间分层筛选
admin.site.register(House, HouseAdmin)

class HousealbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort', 'imgurl', 'status')
    ordering = ('-house', '-sort')
    list_editable = ['sort', 'status']
    list_per_page = 10
admin.site.register(Housealbum, HousealbumAdmin)

class LifetypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort', 'status')
    list_per_page = 10
    ordering = ('-sort','-id')
    list_editable = ['sort', 'status']
    list_filter = ('status',)
    search_fields = ('name',)
admin.site.register(Lifetype,LifetypeAdmin)

class LifeAdmin(admin.ModelAdmin):
    list_display = ('title', 'lifetype', 'keyword', 'status')
    list_per_page = 10
    ordering = ('-id',)
    list_editable = ['lifetype', 'status']
    list_filter = ('status',)
    search_fields = ('name', 'keyword')
admin.site.register(Life,LifeAdmin)

admin.site.register(Customer)

