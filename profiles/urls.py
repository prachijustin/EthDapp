from django.urls import path

from django.contrib.auth import views as auth_views


from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.my_users, name='my_users'),
    path('register/', views.docchainRegister, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new_acc/', views.new_account, name='new_account'),
    path('dashboard/PGDM_certificates/', views.PGDM_generate, name='PGDM_generate'),
    path('dashboard/PGDMHR_certificates/', views.PGDMHR_generate, name='PGDMHR_generate'),
    path('dashboard/PGDMNEW_certificates/', views.PGDMNEW_generate, name='PGDMNEW_generate'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),

]