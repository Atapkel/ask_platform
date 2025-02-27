from django.contrib import admin
from .models import Question, Comment
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description',)



admin.site.register(Question)
admin.site.register(Comment)