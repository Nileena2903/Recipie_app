from django.shortcuts import render
from . models import recipie_tbl

# Create your views here.
def index(request):
    return render(request,'index.html')

def addrecipie(request):
    if request.method=="POST":
        nm=request.POST.get("Rname")
        des=request.POST.get("Rdesc")
        ing=request.POST.get("Ringre")
        im=request.FILES.get("pic")
        ins=request.POST.get("inst")
        obj=recipie_tbl.objects.create(name=nm,desc=des,ingre=ing,img=im,instr=ins)
        obj.save()
        if obj:
            return render(request,'addrecipie.html',{"msg":"Item successfully added"}) 
    return render(request,'addrecipie.html')

def viewrecipie(request):
    ob=recipie_tbl.objects.all()
    return render(request,'view.html',{"recipie":ob})

# def searchrecipie(request):
#     if request.method=='POST':
#         ing = request.POST.get('ing')
#         obb = recipie_tbl.objects.filter(ingre=ing)
#         return render(request,"search.html",{"rec":obb})
#     return render(request,"search.html")
    
def searchrecipie(request):
    rec = []
    if request.method == 'POST':
        ing = request.POST.get('ing', '').strip()
        if ing:
            rec = recipie_tbl.objects.filter(ingre__icontains=ing)
    return render(request, "search.html", {"rec": rec})
