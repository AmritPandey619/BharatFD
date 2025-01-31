from django.db import models
from wagtail.fields import RichTextField  # WYSIWYG support
from wagtail.admin.panels import FieldPanel
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField(blank=True)  # WYSIWYG editor support
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def get_translation(self, lang):
        """Retrieve cached translation or translate dynamically."""
        cache_key = f"faq_{self.id}_{lang}"
        translation = cache.get(cache_key)
        if translation:
            return translation

        translator = Translator()
        translation = {
            "question": translator.translate(self.question, dest=lang).text,
            "answer": translator.translate(self.answer, dest=lang).text
        }
        cache.set(cache_key, translation, timeout=86400)  # Cache for 1 day
        return translation

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
    ]
