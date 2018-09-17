from django.contrib import admin
from FirstApp.models import AccessRecord,Topic,WebPage
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)

