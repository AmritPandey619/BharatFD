from django.urls import path
from .api import FAQListView

urlpatterns = [
    path('api/faqs/', FAQListView.as_view(), name="faq-list"),
]
