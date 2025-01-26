from django.contrib import admin

# Register your models here.
from .models import Visitors, Comment, TodoList

admin.site.register(Visitors)
admin.site.register(Comment)
admin.site.register(TodoList)