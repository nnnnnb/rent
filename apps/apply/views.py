from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse, request
from .models import *
from django.http import JsonResponse
from django.core import paginator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def ajaxmap(request):
    if request.method == 'POST':
        cid = int(request.POST['community_id'])
        ckwargs = {}
        if cid > 0:
            ckwargs['community_id'] = cid
        data = list(House.objects.filter(**ckwargs).values("id", "title",'rental','imgurl'))
        return JsonResponse(data, safe=False)
    

def maps(request):
    data = Community.objects.filter().values('id','name','address','lat','lon')
    context = {
        'data':data
    }
    return render(request, 'maps.html', context)

def lifetext(request): 
    try:
        current = int(request.GET["key"])
    except:
        return redirect(reverse('life', args=[]))
    data = Life.objects.filter(id=current).values('title','content','create_time')[0]
    reclife = Life.objects.filter(status=1).order_by("-click").values('id','title','imgurl')[0:4]
    context = {
        'reclife':reclife,
        'data':data
    }
    return render(request, 'lifetext.html', context)

def life(request):
    lkwargs = {'status':1}
    try:
        current = int(request.GET["page"])
    except:
        current = 1
    try:
        tye = int(request.GET["tye"])
        lkwargs['lifetype_id'] = tye
    except:
        tye = ''
    
    try:
        name = request.GET["name"]
        lkwargs['title__contains'] = name
    except:
        name = ''

    all_dict = Life.objects.filter(**lkwargs).order_by('-create_time').values('id','title','keyword','imgurl','create_time')
    pag = paginator.Paginator(all_dict, 4)
    if current < 1:
        current = 1
    elif current > pag.num_pages:
        current = pag.num_pages

    page = pag.page(current)
    show = 5
    show_start = int(show//2)
    if pag.num_pages > show:
        if current - show_start < 1:
            pageRange = range(1, show)
        elif current + show_start > pag.num_pages:
            pageRange = range(pag.num_pages-show, pag.num_pages+1)
        else:
            pageRange = range(current-show_start, current + show-show_start)
    else:
        pageRange = range(1, pag.num_pages+1)
    
    reclife = Life.objects.filter(status=1).order_by("-click").values('id','title','imgurl')[0:4]
    typedata = Lifetype.objects.filter(status=1).order_by("-sort").values()
    getd = {'tye':tye,'name':name}
    context = {
        "page": page,
        "pageRange": pageRange,
        'typedata':typedata,
        'reclife':reclife,
        'getd':getd
    }
    return render(request, 'life.html', context)

def entiretext(request):
    try:
        current = int(request.GET["key"])
    except:
        return redirect(reverse('entire', args=[]))
    
    housedata = House.objects.filter(status=1,id=current).values()[0]
    houseimg = Housealbum.objects.filter(status=1,house_id=housedata['id']).order_by('-sort').values()

    houfacdata = House_facilities.objects.filter(house_id=housedata['id']).values()
    communitydata = Community.objects.filter(id=housedata['community_id']).values('region_id','block_id','address','name','lat','lon')[0]
    regiondata = Region.objects.filter(id=communitydata['region_id']).values()[0]
    blockdata = Block.objects.filter(id=communitydata['block_id']).values()[0]
      
    facdata = []
    for d in houfacdata:
        fac = Facilities.objects.filter(id=d['facilities_id']).values()[0]
        facdata.append(fac)

    context = {
        'data': housedata,
        'houseimg': houseimg,
        'facdata': facdata,
        'communitydata':communitydata,
        'regiondata':regiondata,
        'blockdata':blockdata
    }
    return render(request, 'entiretext.html', context)

def entire(request):
    try:
        current = int(request.GET["page"])
    except:
        current = 1
    housekwargs = {'status': 1}
    try:
        reg = int(request.GET["reg"])
    except:
        reg = ''
    try:
        blo = int(request.GET["blo"])
    except:
        blo = ''
    try:
        tra = int(request.GET["tra"])
    except:
        tra = ''
    try:
        bed = int(request.GET["bed"])
        housekwargs = {'bedroom': bed}
    except:
        bed = ''
    try:
        ren = int(request.GET["ren"])
    except:
        ren = ''
    try:
        sort = int(request.GET["sort"])
    except:
        sort = ''
    try:
        name = request.GET["name"]
        housekwargs['title__contains'] = name
    except:
        name = ''

    if ren == 1:
        housekwargs['rental__range'] = [0, 1499]
    elif ren == 2:
        housekwargs['rental__range'] = [1500, 1999]
    elif ren == 3:
        housekwargs['rental__gte'] = 2000

    if sort == 1:
        orderby = 'id'
    elif sort == 2:
        orderby = 'rental'
    elif sort == 3:
        orderby = '-rental'
    else:
        orderby = '-id'

    all_data = House.objects.filter(**housekwargs).order_by(orderby).values(
        'id', 'imgurl', 'keyword', 'title', 'rental', 'community')
    all_dict = []
    for d in all_data:
        community = Community.objects.filter(id=d['community']).values()[0]
        if community['region_id'] != reg and reg != '':
            continue
        if community['block_id'] != blo and blo != '':
            continue
        many = Community_traffic.objects.filter(
            community_id=community['id']).values()
        tra_lst = []
        for i in many:
            if tra != i['traffic_id'] and tra != '':
                continue
            traffic_search = Traffic.objects.filter(
                id=i['traffic_id']).values('name')[0]
            tra_lst.append(traffic_search['name'])

        if tra != '' and tra_lst == []:
            continue
        d['many'] = tra_lst
        d['community'] = community['name']
        all_dict.append(d)

    pag = paginator.Paginator(all_dict, 4)

    if current < 1:
        current = 1
    elif current > pag.num_pages:
        current = pag.num_pages

    page = pag.page(current)
    show = 5
    show_start = int(show//2)
    if pag.num_pages > show:
        if current - show_start < 1:
            pageRange = range(1, show)
        elif current + show_start > pag.num_pages:
            pageRange = range(pag.num_pages-show, pag.num_pages+1)
        else:
            pageRange = range(current-show_start, current + show-show_start)
    else:
        pageRange = range(1, pag.num_pages+1)

    tra_data = Traffic.objects.filter(
        status=1).order_by('-sort').values('id', 'name')
    reg_data = Region.objects.filter(
        status=1).order_by('-sort').values('id', 'name')
    blo_data = {}
    if reg:
        blo_data = Block.objects.filter(status=1, region_id=reg).order_by(
            '-sort').values('id', 'name')

    getd = {'reg': reg, 'blo': blo if reg else '', 'tra': tra,
            'bed': bed, 'ren': ren, 'sort': sort, 'name': name}
    context = {
        "page": page,
        "pageRange": pageRange,
        'getd': getd,
        'tra_data': tra_data,
        'reg_data': reg_data,
        'blo_data': blo_data
    }
    return render(request, 'entire.html', context)

def index(request):
    house_data = House.objects.filter(status=1).values(
        'id', 'imgurl', 'title', 'rental', 'community')[0:3]
    house_dict = []
    for d in house_data:
        community = Community.objects.filter(
            id=d['community']).values('name')[0]
        d['community'] = community['name']
        house_dict.append(d)
    life_data = Life.objects.filter(status=1).values(
        'id', 'imgurl', 'title')[0:3]
    context = {
        'house': house_dict,
        'life': life_data
    }
    return render(request, 'index.html', context)

def ajax_region_block_linkage(request, region_id):
    if request.method == 'GET':
        if region_id:
            data = list(Block.objects.filter(
                region_id=region_id).values("id", "name"))
            return JsonResponse(data, safe=False)