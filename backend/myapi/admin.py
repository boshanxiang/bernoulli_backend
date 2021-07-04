from django.contrib import admin
from .models import NaturalPerson, LegalEntity, EquityClass, EquityToken, EmploymentRelation, OfficerRelation, DirectorRelation

admin.site.register(NaturalPerson)
admin.site.register(LegalEntity)
admin.site.register(EquityClass)
admin.site.register(EquityToken)
admin.site.register(EmploymentRelation)
admin.site.register(OfficerRelation)
admin.site.register(DirectorRelation)

# Register your models here.
