from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from assignment_app.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('faq/', include('assignment_app.urls')),
]
