from django.contrib import admin
from django.urls import path,include
from tronj_main import views
urlpatterns = [
    path('index/',views.index,name='index'),
	path('',views.login_redirect,name='login_redirect'),
    path('admin/', admin.site.urls),
    path('Tronj/',include('Tronj.urls')),
]
