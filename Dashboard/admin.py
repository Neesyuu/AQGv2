from django.contrib import admin
from Dashboard.models import PerStudentData, PerQuestionForCertificates, levelUpDec, PerStudentCache, Bookmarked, GotCertificate

# Register your models here.

admin.site.register(PerStudentData)
admin.site.register(levelUpDec)
admin.site.register(PerQuestionForCertificates)
admin.site.register(PerStudentCache)
admin.site.register(Bookmarked)
admin.site.register(GotCertificate)
