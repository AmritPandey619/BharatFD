from django.shortcuts import render
from .models import FAQ

def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'assignment_app/index.html', {'faqs': faqs})
def index(request):
    faqs = FAQ.objects.all()  # Fetch FAQs from the database
    return render(request, 'assignment_app/index.html', {'faqs': faqs})