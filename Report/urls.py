from django.urls import include, path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import MyLoginView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import MyLoginView

urlpatterns = [
    path('user_list',views.user_list),
    path('', views.index, name='index'),
    path('export/excel/', views.export_repair_requests_excel, name='export_excel'),
    path('base',views.base),
    path('copy',views.copy),
    path('copy19',views.copy19),
    path('about',views.about),
    path('pl_admin/', views.pl_admin, name='pl_admin'),
    path('pl_adminlist/', views.pl_adminlist, name='pl_adminlist'),
    path('dashadmin', views.dashadmin, name='dashadmin'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('redirect-after-login/', views.login_redirect, name='login_redirect'),
    path('pl_admin/', views.pl_admin, name='pl_admin'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('repair-form/', views.create_repair_request, name='repair_form'),
    path('repair-table/', views.repair_table, name='repair_table'),
    path('repair/<int:pk>/', views.repair_detail, name='repair_detail'),
    path('login/', views.login_view, name='login'),
    path('create-repair/', views.create_repair_request, name='create_repair'),
    path('repairs/', views.repair_table, name='repair_list'),
    path('repair/edit/<int:id>/', views.repair_edit, name='repair_edit'),
    path('repair/delete/<int:id>/', views.repair_delete, name='repair_delete'),
    path('update-status/<int:id>/', views.update_status, name='update_status'),
    path('dashboard/', views.dashadmin, name='dashboard'),
    path('change_password/', views.change_password, name='change_password'),
    path('my_repairs/', views.my_repairs, name='my_repairs'),
    path('monthly-report-pdf/', views.monthly_report_pdf, name='monthly_report_pdf'),

    

]