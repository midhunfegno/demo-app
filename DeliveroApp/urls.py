from django.urls import path

from DeliveroApp import views

urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('',views.loginpage,name="loginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('logout/',views.logout,name="logout"),
    path('adminregist/',views.adminregist,name="adminregist"),
    path('saveregister/',views.saveregister,name="saveregister"),
    path('admindisplay/',views.admindisplay,name="admindisplay"),
    path('editadmin/<int:dataid>/',views.editadmin,name="editadmin"),
    path('updateadmin/<int:dataid>/',views.updateadmin,name="updateadmin"),
    path('deleteadmin/<int:dataid>/',views.deleteadmin,name="deleteadmin"),
    path('driverregist/',views.driverregist,name="driverregist"),
    path('driverdisplay/',views.driverdisplay,name="driverdisplay"),
    path('savedriverreg/',views.savedriverreg,name="savedriverreg"),
    path('editdriver/<int:dataid>/',views.editdriver,name="editdriver"),
    path('updatedriver/<int:dataid>/',views.updatedriver,name="updatedriver"),
    path('deletedriver/<int:dataid>/',views.deletedriver,name="deletedriver"),
    path('addtasks/', views.addtasks, name="addtasks"),
    path('taskadd/', views.taskadd, name="taskadd"),
    path('viewtask/', views.viewtask, name="viewtask"),
    path('viewmoretask/<int:dataid>/', views.viewmoretask, name="viewmoretask"),
    path('deletetask/<int:dataid>/', views.deletetask, name="deletetask"),
    path('change_preferencenumber/', views.change_preferencenumber, name="change_preferencenumber"),
    path('messagedisplay/', views.messagedisplay, name="messagedisplay"),
    path('Edit_drivercode/', views.Edit_drivercode, name="Edit_drivercode"),
    path('displaydelivered/', views.displaydelivered, name="displaydelivered"),
    path('displayreturned/', views.displayreturned, name="displayreturned"),
]