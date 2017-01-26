from django.contrib import admin
from .models import Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["level","title","slug"]
    list_links = ["level"]
    
    class Meta:
        model = Question
        ordering = ('level',)
        
admin.site.register(Question,QuestionAdmin)