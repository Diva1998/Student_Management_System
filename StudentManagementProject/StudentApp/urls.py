
from django.urls import path

from StudentApp import views

urlpatterns=[
    path('reg',views.register_fun,name='reg'),
    path('regdata',views.regdata_fun),
    path('logdata',views.logdata_fun),
    path('',views.log_fun,name='log'),
    path('home',views.home_fun,name='home'),
    path('add_students',views.addstudent_fun,name='add'),
    path('readdata',views.readdata_fun),
    path('display_student',views.displaystudent_fun,name='display'),
    path('update/<int:id>',views.update_fun,name='update'),
    path('delete/<int:id>',views.delete_fun,name='delete'),
    path('logout',views.log_out_fun,name='log_out')
]