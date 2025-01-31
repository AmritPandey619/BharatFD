from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import FAQ

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")
        query = request.GET.get("q", "")

        faqs = FAQ.objects.all()
        if query:
            faqs = faqs.filter(Q(question__icontains=query) | Q(answer__icontains=query))

        data = []
        for faq in faqs:
            translated = faq.get_translation(lang)
            data.append({
                "id": faq.id,
                "question": translated["question"],
                "answer": translated["answer"]
            })

        return Response({"faqs": data})
