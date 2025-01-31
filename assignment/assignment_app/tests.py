import pytest
from django.urls import reverse
from .models import FAQ

@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(question="What is Django?", answer="A web framework")
    assert faq.question == "What is Django?"
    assert faq.answer == "A web framework"

@pytest.mark.django_db
async def test_faq_api(client):
    FAQ.objects.create(question="What is AI?", answer="Artificial Intelligence")

    response = await client.get(reverse("faq-list") + "?lang=en")
    assert response.status_code == 200
    assert "faqs" in response.json()

@pytest.mark.django_db
async def test_faq_translation():
    faq = FAQ.objects.create(question="What is Machine Learning?", answer="A subset of AI")
    translation = await faq.get_translation("hi") 
    assert "मशीन लर्निंग" in translation["question"]
