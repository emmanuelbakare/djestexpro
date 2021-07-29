from django.contrib import admin
from estate.models import Estate, EstateAdmin, EstateType, Onboarding

# Register your models here.
admin.site.register(Estate)
admin.site.register(EstateAdmin)
admin.site.register(EstateType)
admin.site.register(Onboarding)
