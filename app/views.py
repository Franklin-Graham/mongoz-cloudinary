from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

import pymongo
from django.conf import settings

# Create your views here.
def function(request):

    p = Profile.objects.all()
    db = Main.objects.all()

    page = Paginator(db,12)
    page_number = request.GET.get('page')
    db = page.get_page(page_number)

    por = Portrait.objects.all()
    m = Mandal.objects.all()
    can = Canvas.objects.all()
    bot = Bottle.objects.all()

    d = pymongo.MongoClient(settings.DB_NAME)
    dbs =  d['data']
    collection = dbs['data']

    con = {'Name':'frankuu'}
    collection.insert_one(con)
    return render(request,"index.html",{'img':db,'prof':p,'mandala':m,'portrait':por,'canvas':can,'bottle':bot})