from django.contrib import admin
from .models import Question, Choice

# Register your models here.
"""
注册投票应用(管理后台可以进行编辑)
"""

admin.site.register(Question)
admin.site.register(Choice)