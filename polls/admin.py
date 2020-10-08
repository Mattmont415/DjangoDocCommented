from django.contrib import admin
from .models import Question

# Register your models here.

#Tell the admin that QUestion items have admin interface
admin.site.register(Question)