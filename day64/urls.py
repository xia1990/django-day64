"""day64 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from app01 import views

urlpatterns = [
    # url('',views.index,name='index'),
    url('^publisher_list/',views.publisher_list,name="publisher_list"),
    url('^add_publisher/',views.add_publisher,name="add_publisher"),
    url('^delete_publisher/',views.delete_publisher,name="delete_publisher"),
    url('^edit_publisher/',views.edit_publisher,name="edit_publisher"),
    # 书的对应关系
    url(r'^book_list/', views.book_list, name="book_list"),
    url(r'^add_book/', views.add_book, name="add_book"),
    url(r'^delete_book/', views.delete_book, name="delete_book"),
    url(r'^edit_book/', views.edit_book, name="edit_book"),
]
