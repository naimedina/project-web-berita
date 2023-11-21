from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def all(request):
    if 'cari' in request.GET:
        cari = request.GET['cari']
        berita = models.berita.objects.filter(judul__icontains=cari) 
    else:
        berita = models.berita.objects.all()
    context = {'beritas' : berita}
    return render(request, 'menu/all.html', context)

def isi (request,id):
    berita = get_object_or_404(models.berita,pk=id)
    context = {'beritas' : berita}
    return render(request, "menu/isiberita.html", context)

def trending(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 1
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status = 'publish')
    
    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/trending.html', context)

def sport(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 2
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status = 'publish')
    
    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/sport.html', context)

def politics(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 3
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status = 'publish')
    
    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/politics.html', context)

def lifestyle(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 4
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status = 'publish')
    
    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/lifestyle.html', context)

def healty(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 5
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status = 'publish')
    
    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/healty.html', context)

def entartaiment(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    catID = 6
    if catID :
        berita = models.berita.objects.filter(kategori = catID)
    else :
        berita = models.berita.objects.filter(status = 'publish')
    
    context = {'beritas' : berita, 'kategori' : kategori}

    return render(request, 'menu/entartaiment.html', context)


