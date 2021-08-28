from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #获取url中，hello/ 后面的字符串，传入到这里的name,而这个name变量会传给greet作为变量。
    path("<str:name>", views.greet, name= "greet"),
    path('martin', views.martin, name="martin"),
]
