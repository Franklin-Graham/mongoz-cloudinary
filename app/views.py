from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def function(request):
    m_db = Head.objects.all()

    return render(request,'base.html',{'m_db':m_db})

    # p = Profile.objects.all()
    # db = Main.objects.all()
    #
    # page = Paginator(db,12)
    # page_number = request.GET.get('page')
    # db = page.get_page(page_number)
    #
    # por = Portrait.objects.all()
    # m = Mandal.objects.all()
    # can = Canvas.objects.all()
    # bot = Bottle.objects.all()
    # return render(request,"index.html",{'img':db,'prof':p,'mandala':m,'portrait':por,'canvas':can,'bottle':bot})