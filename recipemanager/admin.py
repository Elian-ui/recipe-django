from django.contrib import admin

from .models import Question, User, Accounts

# Register your models here.
admin.site.register(Question)
admin.site.register(User)
admin.site.register(Accounts)
