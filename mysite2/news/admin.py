from django.contrib import admin
from . models import Customuser, berita, kategori
# Register your models here.


admin.site.register(Customuser)

class kategoriAdmin(admin.ModelAdmin):
    list_display = ['namaKategori']
    search_fields =['namaKategori']


admin.site.register(kategori,kategoriAdmin)


class beritaAdmin(admin.ModelAdmin):
    #list display
    list_display = ['judul','isi','kategori','gambar','penulis']
    search_fields = ['judul','kategori__name']
    autocomplete_fields = ['kategori']

admin.site.register(berita,beritaAdmin)





