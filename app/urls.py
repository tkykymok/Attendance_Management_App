from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('record/', views.recordList, name='record'),
    path('record/admin/', views.records, name='admin_record'),
    path('date_list/admin/', views.datelist, name='admin_date'),
    path('record/update/<int:pk>', views.RecordUpdateView.as_view(), name='record_update'),
    path('record/delete/<int:pk>', views.RecordDeleteView.as_view(), name='record_delete'),
    path('register/', views.staffCreate, name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logput/', views.Logout.as_view(), name='logout'),

    path('password_change/', views.PasswordChange.as_view(), name='password__change'), 
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password__change__done'), 
]