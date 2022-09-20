from django.urls import path
from . import views

#urlconfiguration
urlpatterns ={
    path('',views.say_hello),
    path('EnterFeaures/',views.secondpage),
    path('resultpage/',views.resultpage)


}