from django.contrib import admin
from .models import Question, Choice

# Register your models here.
"""
注册投票应用(管理后台可以进行编辑)
"""

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  # Choice对象将在Question管理页面进行编辑，默认情况，请提供3个Choice对象的编辑区域。

    list_display = ('question_text','pub_date', 'was_published_recently') #定义list列表
    list_filter = ['pub_date'] #对list添加过滤功能，对时间进行过滤
    search_fields = ['question_text'] #添加搜索功能，对问题进行搜索


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

