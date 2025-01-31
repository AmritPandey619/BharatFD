from django.contrib import admin
from .models import FAQ
from modeltranslation.admin import TranslationAdmin
class FAQAdmin(TranslationAdmin):
    list_display = ('question', 'answer', 'created_at')
    search_fields = ('question',)
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('question',)}

admin.site.register(FAQ, FAQAdmin)

