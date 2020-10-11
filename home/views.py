from django.shortcuts import render
from .models import re,allapp,ss,edit,game,aa
# Create your views here.


def index(req):
    return render(req,'index.html')
    
    
def all(req):
    al = aa.objects.all()
    return render(req,'all.html',{'al':al})
    
    
def gam(req):
    gg = aa.objects.filter(appc="game")
    return render(req,'game.html',{'gme':gg})
    
def social(req):
    s = aa.objects.filter(appc="social")
    return render(req,'social.html',{'s':s})
    
    
def editing(req):
    ed = aa.objects.filter(appc="editing")
    return render(req,'editing.html',{'edt':ed})
    
    
def view(req):
    return render(req,'view.html')
    
def cmt(req):
    name = req.POST['name']
    email = req.POST['email']
    msg = req.POST['rew']
    re(name=name,email=email,msg=msg).save()
    return render(req,'index.html')
    
    
def view(req):
    i = req.GET['id']
    ve = aa.objects.filter(id=i)
    return render(req,'view.html',{'kk':ve})