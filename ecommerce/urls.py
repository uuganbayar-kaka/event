from django.contrib import admin
from django.urls import path
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.home_view, name=''),
    path('home', views.home_view, name='home'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='ecom/logout.html'), name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view, name='contactus'),
    path('search', views.search_view, name='search'),
    path('send-feedback', views.send_feedback_view, name='send-feedback'),
    path('view-feedback', views.view_feedback_view, name='view-feedback'),
]
