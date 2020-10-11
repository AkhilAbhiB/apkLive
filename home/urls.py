from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.index),
    path('all',views.all),
    path('game',views.gam),
    path('social',views.social),
    path('editing',views.editing),
    path('view',views.view),
    path('cmt',views.cmt),
    path('view',views.view)
]
