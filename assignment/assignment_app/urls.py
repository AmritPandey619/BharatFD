from django.urls import path
from .api import FAQListView
from .views import index
from .views import faq_list

urlpatterns = [
    path('/', index, name='index'),
    path('faqs/', faq_list, name='index'),
]
