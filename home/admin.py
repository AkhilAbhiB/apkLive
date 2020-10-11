from django.contrib import admin

from .models import re,allapp,ss,edit,game,aa



class reAdmin(admin.ModelAdmin):
    list_display =('name','email','msg')

class allappAdmin(admin.ModelAdmin):
    list_display =('appname','appurl','appdow','appsize')

class ssAdmin(admin.ModelAdmin):
    list_display =('appname','appurl','appdow','appsize')


class editAdmin(admin.ModelAdmin):
    list_display =('appname','appurl','appdow','appsize')


class gameAdmin(admin.ModelAdmin):
    list_display =('appname','appurl','appdow','appsize')



class aaAdmin(admin.ModelAdmin):
    list_display =('appname','appurl','appdow','appsize','appc')


# Register your models here.

admin.site.register(allapp,allappAdmin)
admin.site.register(re,reAdmin)
admin.site.register(ss,ssAdmin)
admin.site.register(edit,editAdmin)
admin.site.register(game,gameAdmin)
admin.site.register(aa,aaAdmin)