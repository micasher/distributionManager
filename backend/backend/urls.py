"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import busines_join,busines_join_whatsapp_link,busines_join_telegram_link
# from admin_dashboard.views import admin_dashboard_schedule,admin_dashboard_message_detail,admin_dashboard_send_messages,admin_dashboard_send_message_detail,admin_dashboard_message_detail_update_send_date
from django.contrib.auth.views import LogoutView, LoginView
from dashboard.views import dashboard_leads_in,dashboard_index,dashboard_messages
# from core.views import test
urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(),name='logout'),
    # path('test', test, name='test'),
    
    path('join/<str:business_slug>/', busines_join, name='business_join'),
    path('join/<str:business_slug>/<str:category_slug>/whatsapp/', busines_join_whatsapp_link, name='business_join_whatsapp'),
    path('join/<str:business_slug>/<str:category_slug>/telegram/', busines_join_telegram_link, name='business_join_telegram'),
    
    path('dashboard', dashboard_index, name='dashboard_index'),
    path('dashboard/leads-in', dashboard_leads_in, name='dashboard_leads_in'),
    path('dashboard/messages', dashboard_messages, name='dashboard_messages'),
    
    # path('admin-dashboard/messages/', admin_dashboard_schedule, name='admin_dashboard_schedule'),
    # path('admin-dashboard/messages/<uuid:id>/change/', admin_dashboard_message_detail, name='message_detail'),
    # path('admin-dashboard/messages/<uuid:id>/update-send-date/', admin_dashboard_message_detail_update_send_date, name='message_update_send_date'),
    # path('admin-dashboard/messages/new/', admin_dashboard_message_detail, name='message_new'),
    
    # path('admin-dashboard/send-messsages/', admin_dashboard_send_messages, name='admin_dashboard_send_messages'),
    # path('admin-dashboard/send-messsages/<uuid:id>/send/', admin_dashboard_send_message_detail,name='admin_dashboard_send_message_detail'),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)