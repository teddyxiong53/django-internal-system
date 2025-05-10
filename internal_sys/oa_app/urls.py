from django.urls import path
from . import views

urlpatterns = [
    path('', views.oa_dashboard, name='oa_home'),  # 新增根路径
    path('announcements/', views.announcement_list, name='announcement_list'),
]