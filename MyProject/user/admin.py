from django.contrib import admin
from .models import *

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Mobile','Message')

admin.site.register(contactus,contactusAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','cname','cpic','cdate')

admin.site.register(category,categoryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','spic','sdate')
    
admin.site.register(slider,sliderAdmin)