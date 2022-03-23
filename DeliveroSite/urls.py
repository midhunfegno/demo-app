from django.urls import path

from DeliveroSite import views

urlpatterns=[
    path('sitehomepage/',views.sitehomepage,name="sitehomepage"),
    path('driverlogin/',views.driverlogin,name="driverlogin"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('sendmessage/',views.sendmessage,name="sendmessage"),
    path('logindriver/',views.logindriver,name="logindriver"),
    path('driverlogout/',views.driverlogout,name="driverlogout"),
    path('viewdrivertasks/',views.viewdrivertasks,name="viewdrivertasks"),
    path('viewtaskdet/<int:taskid>/',views.viewtaskdet,name="viewtaskdet"),
    path('updatedelivered/', views.updatedelivered, name="updatedelivered"),
    path('returndelivered/<int:taskid>/', views.returndelivered, name="returndelivered"),
    path('approvereturn/', views.approvereturn, name="approvereturn"),
]