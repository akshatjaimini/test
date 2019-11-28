from django.shortcuts import render
from hc.models import Sups
#from django.views import generic
# Create your views here.
def log(request):

    if request.method == "POST":
        e = request.POST.get("email")
        p = request.POST.get("p")
        print(e)
        print(p)
        s1 = Sups(un=e,p=p)
        s1.save()
        return render(request,'er.html',None)

    return render(request,'login.html',None)
def sup(request):

    return render(request,'sup.html',None)
